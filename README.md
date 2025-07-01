# 🌾 Crop Disease Identification System

An intelligent web application that uses computer vision and AI to detect crop diseases from leaf images, providing farmers with instant diagnosis and expert agricultural advice in multiple languages.

## 🚀 Features

### 🔍 Disease Detection
- **Real-time Analysis**: Upload crop leaf images for instant disease detection
- **YOLO-based Detection**: Powered by state-of-the-art YOLOv8 object detection model
- **Visual Annotations**: Get annotated images showing detected disease areas with bounding boxes
- **Multi-crop Support**: Supports detection for various crops including:
  - Apple, Bell Pepper, Blueberry, Cherry
  - Corn, Peach, Potato, Raspberry
  - Soybean, Strawberry, Tomato, Grape

### 🤖 AI Agricultural Assistant
- **Expert Consultation**: Chat with an AI agricultural advisor specialized in plant diseases
- **Multilingual Support**: Available in English and Japanese (日本語)
- **Contextual Advice**: Get specific guidance based on detected diseases
- **Quick Actions**: One-click access to disease information and prevention tips

### 🎨 User Experience
- **Modern Interface**: Clean, responsive design with intuitive navigation
- **Real-time Processing**: Fast image analysis and instant results
- **Mobile Friendly**: Works seamlessly on desktop and mobile devices
- **Dark Theme**: Professional dark background with white content containers

## 🛠️ Technology Stack

- **Frontend**: Streamlit (Python web framework)
- **Computer Vision**: YOLOv8 (Ultralytics)
- **AI Chat**: LangChain + Groq (Llama 3.1 8B)
- **Image Processing**: OpenCV, PIL
- **Languages**: Python

## 📋 Prerequisites

- Python 3.8 or higher
- Groq API key (for AI chatbot functionality)

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/JacobAsir/Crop-Disease.git
   cd Crop-Disease
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Download the trained model**
   - Ensure `best.pt` (YOLO model weights) is in the root directory
   - This file contains the trained weights for crop disease detection

## 🚀 Usage

1. **Start the application**
   ```bash
   streamlit run app.py
   ```

2. **Access the web interface**
   - Open your browser and navigate to `http://localhost:8501`

3. **Upload and analyze**
   - Upload a crop leaf image (JPG, JPEG, or PNG)
   - Click "Process" to detect diseases
   - View annotated results with detected diseases

4. **Get expert advice**
   - Use the AI assistant to ask questions about detected diseases
   - Switch between English and Japanese for multilingual support
   - Get prevention tips and treatment recommendations

## 📁 Project Structure

```
crop-disease-identification/
├── app.py                 # Main Streamlit application
├── model.py              # YOLO model inference functions
├── chatbot.py            # AI chatbot implementation
├── utils.py              # Disease information and utilities
├── requirements.txt      # Python dependencies
├── best.pt              # Trained YOLO model weights
├── .env                 # Environment variables (create this)
└── README.md            # Project documentation
```

## 🎯 Supported Diseases

### Healthy Crops
- Apple, Bell Pepper, Blueberry, Cherry, Corn, Peach, Potato, Raspberry, Soybean, Strawberry, Tomato, Grape

### Disease Detection
- **Apple**: Scab, Rust
- **Bell Pepper**: Leaf Spot
- **Corn**: Gray Leaf Spot, Leaf Blight, Rust
- **Potato**: Early Blight, Late Blight
- **Squash**: Powdery Mildew
- **Tomato**: Early Blight, Septoria Leaf Spot, Bacterial Spot, Late Blight, Mosaic Virus, Yellow Virus, Mold, Spider Mites
- **Grape**: Black Rot

## 🌐 Multilingual Support

The application supports:
- **English**: Full interface and AI responses
- **Japanese (日本語)**: Complete localization including UI and expert advice

## 🔑 API Keys

To use the AI chatbot feature, you need a Groq API key:
1. Sign up at [Groq Console](https://console.groq.com/)
2. Generate an API key
3. Add it to your `.env` file

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Ultralytics** for the YOLOv8 framework
- **Groq** for fast AI inference
- **LangChain** for AI application development
- **Streamlit** for the web framework


**Made with ❤️ for farmers and agricultural professionals worldwide**
