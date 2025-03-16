from fastapi import FastAPI, File, UploadFile
import uvicorn
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from image_processor import classify_stone


import shutil
import os

app = FastAPI()

UPLOAD_DIR = "uploads/"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def home():
    return {"message": "Stone Classification API"}

@app.post("/classify/")
def classify(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    classification_result = classify_stone(file_path)
    
    return {"filename": file.filename, "classification": classification_result}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


