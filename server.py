'''
This file contains the Flask server code for the Emotion Detection application.
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def emo_detector():
    '''
    Runs emotion detection over it using emotion_detector() function.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is 'anger': {anger_score}, "
        f"'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} and "
        f"'sadness': {sadness_score}. The dominant emotion is <b>{dominant_emotion}</b>."
    )

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')
