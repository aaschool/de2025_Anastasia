from fastapi import FastAPI, File, UploadFile, Form
import uvicorn
import sys
import os
import json
import shutil
import subprocess  # To trigger the Arducam capture script

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from image_processor import classify_stone

app = FastAPI()

UPLOAD_DIR = "uploads/"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def home():
    return {"message": "Stone Classification API"}

# Start Arducam Tof Camera Using capture_raw.py
@app.post("/start_camera/")
def start_camera():
    """
    Starts the Arducam ToF camera to capture an image.
    Runs an external script that captures and saves an image.
    """
    try:
        subprocess.Popen(["python3", "hardware/capture_raw.py"])  # Correct path to your script
        return {"message": "Camera started! Fetch image when ready."}
    except Exception as e:
        return {"error": str(e)}

# Serve the Latest Captured Image
@app.get("/latest_image/")
def get_latest_image():
    """
    Returns the latest captured image URL.
    """
    image_path = "test_images/captured_image.jpg"  # The latest saved image
    if os.path.exists(image_path):
        return {"image_url": f"http://localhost:8000/{image_path}"}
    else:
        return {"error": "No image found"}

# Classify the Uploaded Image
@app.post("/classify/")
def classify(file: UploadFile = File(...), dimensions: str = Form(...)):
    """
    Receives an image file and dimensions, then returns the classification along with dimensions.
    """
    # Convert JSON string to dictionary
    dimensions_data = json.loads(dimensions)

    # Save the uploaded file
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # Classify the image
    classification_result = classify_stone(file_path)
    
    return {
        "filename": file.filename,
        "classification": classification_result,
        "dimensions": dimensions_data
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
