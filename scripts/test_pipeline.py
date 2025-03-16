import requests
import json

# Define API endpoint
API_URL = "http://127.0.0.1:8000/classify/"

# Define test image path
import os

# Use a sample image if camera capture fails
TEST_IMAGE = "test_images/captured_image.jpg" if os.path.exists("test_images/captured_image.jpg") else "test_images/sample_stone.jpg"


# Read dimensions from the file where capture_raw.py stores them
dimensions_file = "test_images/dimensions.json"

if os.path.exists(dimensions_file):
    with open(dimensions_file, "r") as f:
        object_dimensions = json.load(f)  # Load real dimensions
else:
    object_dimensions = {"width": 0, "height": 0, "depth": 0}  # Default values

# Convert dimensions to JSON format
dimensions_json = json.dumps(object_dimensions)

# Open and send the image to the API
with open(TEST_IMAGE, "rb") as image_file:
    files = {"file": image_file}
    data = {"dimensions": json.dumps(object_dimensions)}  # Send dimensions as JSON
    response = requests.post(API_URL, files=files)

# Print the response from the server
print("API Response:", response.json())
