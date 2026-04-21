# AI Emotion Detection Web App

This project is a web application that detects emotions from text using IBM Watson NLP.

## Features
- Detects emotions (joy, sadness, anger, fear, disgust)
- Returns dominant emotion
- Flask-based web API

## Technologies Used
- Python
- Flask
- IBM Watson NLP
- unittest
- pylint

## How to Run
1. Install dependencies:
   pip install -r requirements.txt

2. Run the app:
   python app.py

## Example Output
{
  "joy": 0.85,
  "sadness": 0.02,
  "anger": 0.05,
  "fear": 0.03,
  "disgust": 0.05,
  "dominant_emotion": "joy"
}
