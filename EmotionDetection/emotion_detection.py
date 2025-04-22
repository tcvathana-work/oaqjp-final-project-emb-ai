'''
This file contains the emotion detection function that interacts with the Watson API.
It sends a request to the Watson API with the text to analyze.
And returns the emotion scores and the dominant emotion.
'''
import json
import requests

def emotion_detector(text_to_analyse):
    '''
    Takes a string as input and returns the emotion scores and the dominant emotion.
    '''
    base_url = 'https://sn-watson-emotion.labs.skills.network'
    url = f'{base_url}/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    body = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, headers=headers, json=body, timeout=10)

    anger_score = None
    disgust_score = None
    fear_score = None
    joy_score = None
    sadness_score = None
    dominant_emotion = None
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']

        # Determine the dominant emotion
        emotions = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        dominant_emotion = max(emotions, key=emotions.get)
    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
