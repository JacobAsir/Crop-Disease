from ultralytics import YOLO
import cv2

# Load YOLO model
model = YOLO("best.pt")  # Replace with your model path

# YOLO inference functions
import numpy as np

def detect_disease(image_bytes):
    # Decode image bytes to numpy array
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Save to a temporary file for YOLO model if it only accepts file paths
    # Otherwise, modify YOLO model to accept image directly
    # For now, we'll save to a temp file as the model expects a path
    import tempfile
    import os
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_img_file:
        cv2.imwrite(temp_img_file.name, img)
        image_path = temp_img_file.name

    try:
        results = model(image_path)
    finally:
        os.remove(image_path)
    detected_diseases = []
    for result in results:
        for box in result.boxes:
            class_id = int(box.cls)
            confidence = box.conf.item()
            disease_name = result.names[class_id]
            detected_diseases.append({"disease": disease_name, "confidence": confidence})
    return detected_diseases, results

def save_annotated_image(results, original_image_bytes, output_path):
    nparr = np.frombuffer(original_image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    for result in results:
        img = result.plot()  # Draw bounding boxes and labels
    cv2.imwrite(output_path, img)
    return output_path