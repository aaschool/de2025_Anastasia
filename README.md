# **Material Evaluation System**

## **Project Overview**
This project automates the evaluation of dismantled stones, classifying their reusability and providing precise measurements using machine learning and depth field imaging. By leveraging an **Arducam TOF Camera** and **Raspberry Pi**, the system captures depth images, processes them with an AI model, and provides **real-time feedback** on whether a stone is reusable along with its exact **dimensions (length, width, height, and depth).**

## **Required Components**

### **Hardware**
- **Arducam TOF Camera** – Captures depth images for measurement & classification.
- **Raspberry Pi** – Runs AI model & processes stone data.
- **Power Source** – Provides power to Raspberry Pi.
- **LED Indicator** – Green/red light feedback system.

### **Software**
- **Python 3.x** – For backend API and ML processing.
- **Flask or FastAPI** – Handles API requests.
- **OpenCV & TensorFlow** – Image processing & AI classification.
- **React.js** – Frontend UI for users.

## **Key Features**
- **AI-Based Image Classification** – Determines if a stone is reusable.
- **Accurate Stone Measurement** – Provides precise length, width, height, and depth.
- **Depth Field Analysis** – Extracts detailed stone dimensions.
- **Automated Labeling System** – Provides real-time feedback via LED indicator.
- **Raspberry Pi Processing** – Runs AI model locally, no cloud dependencies.
- **Data Storage & Cataloging** – Organizes and stores stone evaluation data.
