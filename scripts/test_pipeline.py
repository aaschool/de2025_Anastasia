import requests

# Define API endpoint
API_URL = "http://127.0.0.1:8000/classify/"

# Define test image path
TEST_IMAGE = "test_images/sample_stone.jpg"

# Open and send the image to the API
with open(TEST_IMAGE, "rb") as image_file:
    files = {"file": image_file}
    response = requests.post(API_URL, files=files)

# Print the response from the server
print("API Response:", response.json())
