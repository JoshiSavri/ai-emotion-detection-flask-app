# Final Project

## AI Emotion Detection Web Application

This project is part of the Final Project for the course. It implements an AI-based web application that detects emotions from text using Watson NLP.

---

## 📌 Features

- Detects emotions from input text:
  - Joy
  - Sadness
  - Anger
  - Fear
  - Disgust
- Identifies the dominant emotion
- Web API built using Flask
- Error handling for invalid input
- Unit testing included
- Static code analysis using pylint

---

## 🛠️ Technologies Used

- Python
- Flask
- Requests Library
- Watson NLP API
- unittest
- pylint

---

## 🚀 How It Works

1. User sends text input
2. Application sends request to Watson NLP API
3. API returns emotion scores
4. Application processes and returns formatted output

---

## 📊 Example Output

```json
{
  "sadness": 0.02,
  "joy": 0.90,
  "fear": 0.03,
  "disgust": 0.01,
  "anger": 0.04,
  "dominant_emotion": "joy"
}
