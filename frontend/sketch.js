let img; // Variable to hold the uploaded image
let statusText = "Waiting for image from Arducam...";

function setup() {
    createCanvas(600, 400);
    background(220);
    textSize(16);
    textAlign(CENTER, CENTER);
    text(statusText, width / 2, height / 2);
    
    // Add Start Camera Button
    let startButton = createButton("Start Camera");
    startButton.position(20, 400);
    startButton.mousePressed(startCamera);
    styleButton(startButton, "#28a745", "#1e7e34"); // Green button

    // Add Button to Fetch Image from Backend
    let fetchButton = createButton("Fetch Arducam Image");
    fetchButton.position(20, 450);
    fetchButton.mousePressed(fetchImage);
    styleButton(fetchButton, "#17a2b8", "#117a8b"); // Blue-cyan button

    // Add Analyze Stone Button
    let analyzeButton = createButton("Analyze Stone");
    analyzeButton.position(180, 450);
    analyzeButton.mousePressed(analyzeImage);
    styleButton(analyzeButton, "#ffc107", "#d39e00"); // Yellow button

    // Add Data Display Area
    let dataDiv = createDiv("<h3>Analysis Results:</h3><p id='dataOutput'></p>");
    dataDiv.position(20, 500);
    dataDiv.style("font-size", "18px");
    dataDiv.style("padding", "10px");
}

// Send request to start the Arducam camera on the backend
async function startCamera() {
    try {
        let response = await fetch("http://localhost:8000/start_camera", { method: "POST" });
        let result = await response.json();
        statusText = result.message;
    } catch (error) {
        console.error("Error:", error);
        alert("Error starting the camera.");
    }
}

// Fetch the latest depth image from the backend
function fetchImage() {
    statusText = "Fetching image...";
    loadImage("http://localhost:8000/latest_image/", img => {
        image(img, 0, 0, width, height);
        statusText = "Image Loaded! Click 'Analyze Stone'.";
    }, () => {
        statusText = "Failed to load image.";
    });
}

// Send image for analysis using existing API
async function analyzeImage() {
    let formData = new FormData();
    formData.append("file", "http://localhost:8000/latest_image"); // Sending image URL

    try {
        let response = await fetch("http://localhost:8000/analyze", {
            method: "POST",
            body: formData
        });
        let result = await response.json();
        document.getElementById("dataOutput").innerHTML = `
            Condition: ${result.condition}<br>
            Dimensions: ${result.dimensions}<br>
            Status: <span style='color:${result.status === 'usable' ? 'green' : 'red'}'>${result.status}</span>
        `;
    } catch (error) {
        console.error("Error:", error);
        alert("Error analyzing the image.");
    }
}

// Function to style buttons with custom colors
function styleButton(button, bgColor, hoverColor) {
    button.style("padding", "10px 20px");
    button.style("background", bgColor);
    button.style("color", "white");
    button.style("font-size", "16px");
    button.style("border", "none");
    button.style("border-radius", "5px");
    button.style("cursor", "pointer");
    button.mouseOver(() => button.style("background", hoverColor));
    button.mouseOut(() => button.style("background", bgColor));
}
