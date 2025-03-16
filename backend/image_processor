import torch
from torchvision import transforms
from PIL import Image
import os

# Load the trained machine learning model
MODEL_PATH = "models/trained_model.pth"
model = torch.load(MODEL_PATH, map_location=torch.device('cpu'))
model.eval()

# Define image preprocessing function
def preprocess_image(image_path):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),  # Resize image to 224x224 pixels
        transforms.ToTensor(),          # Convert image to tensor
        transforms.Normalize(mean=[0.5], std=[0.5])  # Normalize
    ])
    image = Image.open(image_path).convert("RGB")
    return transform(image).unsqueeze(0)  # Add batch dimension

# Define function to classify stone
def classify_stone(image_path):
    if not os.path.exists(image_path):
        return "Error: File not found"
    
    image_tensor = preprocess_image(image_path)
    with torch.no_grad():
        output = model(image_tensor)
        predicted_class = torch.argmax(output, dim=1).item()
    
    # Map numerical class to label (adjust based on training labels)
    class_labels = {0: "Not Reusable", 1: "Reusable"}
    return class_labels.get(predicted_class, "Unknown Classification")
