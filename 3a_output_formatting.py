# 3a_output_formatting.py

from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions

def emotion_detector(text_to_analyze):
    """
    This function analyzes text and returns formatted emotion output.
    """

    if not text_to_analyze:
        return {
            "sadness": None,
            "joy": None,
            "fear": None,
            "disgust": None,
            "anger": None,
            "dominant_emotion": None
        }

    try:
        # Replace with your API key and URL
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

    except Exception:
        return {
            "sadness": None,
            "joy": None,
            "fear": None,
            "disgust": None,
            "anger": None,
            "dominant_emotion": None
        }
