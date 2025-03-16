import cv2
import numpy as np
import ArducamDepthCamera as ac

# Initialize the camera
camera = ac.ArducamDepthCamera()
camera.start(stream=True)

# Capture an image
ret, depth_frame = camera.get_depth_frame()
if not ret:
    print("Error: Could not capture depth frame")
    camera.close()
    exit()

# Save the depth frame
cv2.imwrite("test_images/captured_depth.jpg", depth_frame)

# Capture RGB image
ret, color_frame = camera.get_color_frame()
if not ret:
    print("Error: Could not capture color frame")
    camera.close()
    exit()

# Save the color image
cv2.imwrite("test_images/captured_image.jpg", color_frame)

# Process the depth image to detect object dimensions
def measure_object_dimensions(depth_frame):
    # Convert depth data to a numpy array
    depth_array = np.array(depth_frame, dtype=np.uint16)

    # Thresholding to segment the object
    _, binary = cv2.threshold(depth_array, 20, 255, cv2.THRESH_BINARY)

    # Find contours (edges of the object)
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) == 0:
        print("No object detected.")
        return None

    # Get the largest contour (assuming it's the object)
    largest_contour = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(largest_contour)

    # Convert pixel width & height to real-world mm using depth data
    depth_value = np.mean(depth_array[y:y+h, x:x+w])  # Average depth
    scale_factor = 0.1  # This value depends on camera calibration

    real_width = w * scale_factor
    real_height = h * scale_factor
    real_depth = depth_value * scale_factor

    return real_width, real_height, real_depth

# Get dimensions
dimensions = measure_object_dimensions(depth_frame)

if dimensions:
    real_width, real_height, real_depth = dimensions
    print(f"Object Dimensions (mm): Width={real_width:.2f}, Height={real_height:.2f}, Depth={real_depth:.2f}")

import json
import os

# Ensure the test_images directory exists
os.makedirs("test_images", exist_ok=True)

# Save dimensions to a JSON file for later use
if dimensions:
    dimensions_data = {
        "width": real_width,
        "height": real_height,
        "depth": real_depth
    }

    with open("test_images/dimensions.json", "w") as f:
        json.dump(dimensions_data, f)

    print(f"Saved dimensions to test_images/dimensions.json: {dimensions_data}")


camera.close()
