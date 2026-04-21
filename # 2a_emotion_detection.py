# 2a_emotion_detection.py

import requests

def emotion_detector(text_to_analyse):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    json_data = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    response = requests.post(url, headers=headers, json=json_data)

    if response.status_code == 200:
        emotions = response.json()["emotionPredictions"][0]["emotion"]

        sadness = emotions["sadness"]
        joy = emotions["joy"]
        fear = emotions["fear"]
        disgust = emotions["disgust"]
        anger = emotions["anger"]

        dominant_emotion = max(emotions, key=emotions.get)

        return {
            "sadness": sadness,
            "joy": joy,
            "fear": fear,
            "disgust": disgust,
            "anger": anger,
            "dominant_emotion": dominant_emotion
        }

    else:
        return {
            "sadness": None,
            "joy": None,
            "fear": None,
            "disgust": None,
            "anger": None,
            "dominant_emotion": None
        }
