import streamlit as st
import os
from PIL import Image
from model import detect_disease, save_annotated_image
from chatbot import chatbot
from utils import class_info_dict, get_disease_info

# Page configuration
st.set_page_config(
    page_title="Crop Disease Identification",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for consistent white container theme
st.markdown("""
    <style>
    /* Main container styling */
    .main {
        padding: 1rem;
        background-color: #1a1a1a;
    }
    
    /* White container for all content */
    .stApp > main > div > div > div {
        background-color: white;
        border-radius: 10px;
        padding: 2rem;
        margin: 1rem 0;
    }
    
    /* Title styling */
    h1 {
        color: #333;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    h3 {
        color: #333;
    }
    
    /* Button styling */
    .stButton > button {
        background-color: #0066cc;
        color: white;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        border: none;
        font-weight: 500;
        width: 100%;
    }
    
    .stButton > button:hover {
        background-color: #0052a3;
    }
    
    /* File uploader styling */
    .stFileUploader {
        background-color: #f8f9fa;
        border: 2px dashed #dee2e6;
        border-radius: 8px;
        padding: 1rem;
    }
    
    /* Chat container styling */
    .chat-container {
        background-color: #f5f5f5;
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        padding: 1rem;
        height: 400px;
        overflow-y: auto;
    }
    
    /* Info box styling - FIXED to ensure visibility */
    .stAlert {
        background-color: #e3f2fd !important;
        color: #1976d2 !important;
        border-radius: 8px !important;
        border: 1px solid #bbdefb !important;
        padding: 1rem !important;
        margin: 1rem 0 !important;
        position: relative !important;
        z-index: 10 !important;
    }
    
    /* Column styling */
    [data-testid="column"] {
        background-color: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Dark background for main app */
    [data-testid="stAppViewContainer"] {
        background-color: #1a1a1a;
    }
    
    [data-testid="stHeader"] {
        background-color: #1a1a1a;
    }
    
    /* Image styling */
    .stImage {
        border-radius: 8px;
        overflow: hidden;
    }
    
    /* Fix for info message visibility */
    div[data-testid="stAlert"] {
        background-color: #e3f2fd !important;
        border: 1px solid #bbdefb !important;
        margin-bottom: 1rem !important;
    }
    
    div[data-testid="stAlert"] p {
        color: #1976d2 !important;
        margin: 0 !important;
    }
    
    /* Language selector styling */
    .stSelectbox {
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'processed' not in st.session_state:
    st.session_state.processed = False
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'detected_diseases' not in st.session_state:
    st.session_state.detected_diseases = []
if 'image_bytes' not in st.session_state:
    st.session_state.image_bytes = None
if 'language' not in st.session_state:
    st.session_state.language = "English"

# Title
st.markdown("<h1>Crop Disease Identification</h1>", unsafe_allow_html=True)

# Create main container
with st.container():
    # Create two columns with spacing
    col1, spacer, col2 = st.columns([5, 0.5, 5])
    
    # Left column - Image upload and processing
    with col1:
        # Preview section
        st.markdown("### 🌾 Preview")
        
        # File uploader with custom styling
        uploaded_file = st.file_uploader(
            "Choose file", 
            type=["jpg", "jpeg", "png"], 
            key="file_uploader",
            help="Upload an image of a crop leaf to detect diseases"
        )
        
        if uploaded_file is not None:
            # Read and store image bytes
            image_bytes = uploaded_file.getvalue()
            st.session_state.image_bytes = image_bytes
            
            # Display uploaded image
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_container_width=True)
            
            # Process button
            if st.button("Process", type="primary", use_container_width=True):
                with st.spinner("Processing image..."):
                    # Perform disease detection
                    detected_diseases, results = detect_disease(st.session_state.image_bytes)
                    st.session_state.detected_diseases = detected_diseases
                    st.session_state.processed = True
                    
                    # Save annotated image
                    output_path = "annotated_image.jpg"
                    save_annotated_image(results, st.session_state.image_bytes, output_path)
                    
                    # Store the annotated image path
                    st.session_state.annotated_image_path = output_path
        
        # Display processed image if available
        if st.session_state.processed and hasattr(st.session_state, 'annotated_image_path'):
            st.markdown("### Processed Image")
            
            # Create caption with detected diseases
            if st.session_state.detected_diseases:
                diseases_list = [d["disease"] for d in st.session_state.detected_diseases]
                caption = f"**Detected Diseases:** {', '.join(diseases_list)}"
            else:
                caption = "**No diseases detected**"
            
            # Display annotated image
            if os.path.exists(st.session_state.annotated_image_path):
                st.image(st.session_state.annotated_image_path, caption=caption, use_container_width=True)
    
    # Spacer column
    with spacer:
        st.empty()
    
    # Right column - Chatbot interface
    with col2:
        st.markdown("### 💬 Disease Assistant")
        
        # Language selector
        language = st.selectbox(
            "Select Language / 言語を選択",
            ["English", "Japanese"],
            index=0 if st.session_state.language == "English" else 1,
            key="language_selector"
        )
        st.session_state.language = language
        
        if st.session_state.processed and st.session_state.detected_diseases:
            # Show detected diseases with custom styling to ensure visibility
            diseases_text = ', '.join([d['disease'] for d in st.session_state.detected_diseases])
            
            # Display disease info based on language
            if st.session_state.language == "Japanese":
                label = "検出された病害："
            else:
                label = "Detected Diseases:"
                
            st.markdown(
                f"""
                <div style='background-color: #e3f2fd; 
                           color: #1976d2; 
                           padding: 1rem; 
                           border-radius: 8px; 
                           border: 1px solid #bbdefb;
                           margin-bottom: 1rem;'>
                    <strong>{label}</strong> {diseases_text}
                </div>
                """, 
                unsafe_allow_html=True
            )
            
            # Quick action buttons with language support
            if st.session_state.language == "Japanese":
                st.markdown("**どのようにお手伝いできますか？**")
                btn1_text = "この病気は何ですか？"
                btn2_text = "予防のヒント"
            else:
                st.markdown("**How can we assist you?**")
                btn1_text = "What is this disease?"
                btn2_text = "Prevention tips"
            
            col_btn1, col_btn2 = st.columns(2)
            with col_btn1:
                if st.button(btn1_text, use_container_width=True):
                    # Get the first detected disease
                    disease = st.session_state.detected_diseases[0]["disease"]
                    disease_info = get_disease_info(disease, st.session_state.language)
                    
                    # Add to chat history
                    st.session_state.chat_history.append({
                        "role": "user",
                        "content": btn1_text
                    })
                    st.session_state.chat_history.append({
                        "role": "assistant",
                        "content": disease_info
                    })
                    st.rerun()
            
            with col_btn2:
                if st.button(btn2_text, use_container_width=True):
                    disease = st.session_state.detected_diseases[0]["disease"]
                    
                    if st.session_state.language == "Japanese":
                        prevention_query = f"{disease}を将来的に防ぐにはどうすればよいですか？"
                    else:
                        prevention_query = f"How can I prevent {disease} in the future?"
                    
                    # Add to chat history
                    st.session_state.chat_history.append({
                        "role": "user",
                        "content": prevention_query
                    })
                    
                    # Get response from chatbot with language parameter
                    disease_info = class_info_dict.get(disease, "")
                    response = chatbot(prevention_query, st.session_state.chat_history, disease_info, st.session_state.language)
                    
                    st.session_state.chat_history.append({
                        "role": "assistant",
                        "content": response
                    })
                    st.rerun()
            
            # Create a container for chat messages with fixed height
            st.markdown("---")
            
            # Chat messages container with scroll
            chat_container = st.container(height=400)
            with chat_container:
                # Display chat messages
                for message in st.session_state.chat_history:
                    with st.chat_message(message["role"]):
                        st.markdown(message["content"])
            
            # Chat input outside the scrollable container
            placeholder = "メッセージを入力..." if st.session_state.language == "Japanese" else "Type a message..."
            user_question = st.chat_input(placeholder, key="chat_input")
            
            if user_question:
                # Add user message to chat history
                st.session_state.chat_history.append({
                    "role": "user",
                    "content": user_question
                })
                
                # Get chatbot response with language parameter
                with st.spinner("考え中..." if st.session_state.language == "Japanese" else "Thinking..."):
                    disease = st.session_state.detected_diseases[0]["disease"]
                    disease_info = class_info_dict.get(disease, "")
                    response = chatbot(user_question, st.session_state.chat_history, disease_info, st.session_state.language)
                    
                    # Add assistant response to chat history
                    st.session_state.chat_history.append({
                        "role": "assistant",
                        "content": response
                    })
                
                st.rerun()
        
        else:
            # Empty state with consistent styling
            if st.session_state.language == "Japanese":
                empty_message = "👈 会話を開始するには、画像をアップロードして処理してください"
            else:
                empty_message = "👈 Please upload and process an image to start the conversation"
                
            st.markdown(
                f"""
                <div style='text-align: center; padding: 3rem; background-color: #f5f5f5; border-radius: 10px; margin-top: 2rem;'>
                    <p style='color: #666; font-size: 1.1rem;'>
                        {empty_message}
                    </p>
                </div>
                """, 
                unsafe_allow_html=True
            )

# Add footer spacing
st.markdown("<br><br>", unsafe_allow_html=True)
