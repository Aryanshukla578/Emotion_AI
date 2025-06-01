from transformers import pipeline
import random

def detect_emotion(text):
    classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=False)
    result = classifier(text)[0]
    return result['label'], result['score']

def generate_expression(emotion):
    templates = {
        "joy": ["A sunrise dancing on calm waters.", "A field bursting into golden laughter."],
        "sadness": ["Rain on forgotten pages.", "A candle flickering in a silent chapel."],
        "anger": ["A volcano swallowing the sky.", "A tiger pacing in a cage of fire."],
        "fear": ["Shadows that whisper your name.", "Storm clouds that refuse to pass."],
        "love": ["A heartbeat painted in rose gold.", "Soft eyes in a field of stars."],
        "neutral": ["A mirror reflecting peaceful stillness."]
    }
    return random.choice(templates.get(emotion.lower(), ["A drifting memory shaped as silence."]))