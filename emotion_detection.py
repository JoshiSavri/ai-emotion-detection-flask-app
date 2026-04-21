# 2a_emotion_detection.py

from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions

def emotion_detector(text_to_analyze):
    """
    This function analyzes the input text and returns detected emotions.
    """

    if not text_to_analyze:
        return {
            "error": "Invalid input"
        }

    try:
        # Replace with your actual API key and URL
        authenticator = IAMAuthenticator('YOUR_API_KEY')
        nlu = NaturalLanguageUnderstandingV1(
            version='2021-08-01',
            authenticator=authenticator
        )
        nlu.set_service_url('YOUR_URL')

        response = nlu.analyze(
            text=text_to_analyze,
            features=Features(emotion=EmotionOptions())
        ).get_result()

        emotions = response["emotion"]["document"]["emotion"]

        return {
            "sadness": emotions["sadness"],
            "joy": emotions["joy"],
            "fear": emotions["fear"],
            "disgust": emotions["disgust"],
            "anger": emotions["anger"],
            "dominant_emotion": max(emotions, key=emotions.get)
        }

    except Exception as e:
        return {
            "error": str(e)
        }
