from fastapi import FastAPI, File, UploadFile, Form
import uvicorn
import sys
import os
import json
import shutil

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from image_processor import classify_stone

app = FastAPI()

UPLOAD_DIR = "uploads/"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def home():
    return {"message": "Stone Classification API"}

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
