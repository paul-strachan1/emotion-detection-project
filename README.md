# Repository for final project

Course: IBM Generative AI Engineering
Module: Developing AI applications with Python and Flask
This is my completed assignment for the Developing AI Applications with Python and Flask module

# Emotion Detection Web Application

## Overview
This project is a web application that analyzes the emotional content of text using natural language processing. It provides a user-friendly interface where users can input text and receive an analysis of the emotions expressed in that text.

## Features
- Text-based emotion analysis
- Detection of five primary emotions: anger, disgust, fear, joy, and sadness
- Identification of the dominant emotion in the text
- Simple and intuitive web interface
- Real-time analysis using IBM Watson NLP API

## Technologies Used
- Python 3.x
- Flask web framework
- IBM Watson NLP API for emotion detection
- HTML/CSS for the frontend
- RESTful API architecture

## Project Structure

final_project/
├── emotion_detection.py # Core emotion detection functionality
├── server.py # Flask server implementation
├── test_emotion_detection.py # Unit tests
├── static/ # Static assets (CSS, JS)
├── templates/ # HTML templates
│ └── index.html # Main application page
└── README.md # Project documentation

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/emotion-detection-project.git
   cd emotion-detection-project
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your environment variables (if needed):
   ```
   export FLASK_APP=server.py
   export FLASK_ENV=development
   ```

## Usage
1. Start the Flask server:
   ```
   python server.py
   ```

2. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

3. Enter text in the input field and click "Analyze" to see the emotion analysis results.

## API Endpoints
- `GET /`: Renders the main application page
- `GET /emotionDetector?textToAnalyze=<text>`: Analyzes the provided text and returns emotion scores

## Testing
Run the unit tests with:

## Course Information
This project was developed as part of the IBM Generative AI Engineering course, specifically for the "Developing AI Applications with Python and Flask" module.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- IBM Watson NLP API for providing the emotion detection capabilities
- Flask framework for the web application structure
- IBM Generative AI Engineering course for the learning materials and guidance
