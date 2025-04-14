import requests
import json

def emotion_detector(text_to_analyse):
    # Define the URL for the sentiment analysis API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Make a POST request to the API with the payload
    response = requests.post(url, json=myobj, headers=header)
    
    # Check if the response status code is 200 (success)
    if response.status_code == 200:
        # Parse the response from the API
        formatted_response = json.loads(response.text)
        
        # Extract the emotions and their scores
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        
        # Find the dominant emotion (emotion with the highest score)
        dominant_emotion = max(emotions, key=emotions.get)
        
        # Extract individual emotions along with their scores
        anger_score = emotions['anger']
        disgust_score = emotions['disgust']
        fear_score = emotions['fear']
        joy_score = emotions['joy']
        sadness_score = emotions['sadness']
    # Check if the response status code is 500
    # 500 is the error code for a blank entry, not 400 as documented in the course
    elif response.status_code == 500:
        # Set all values to None
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None
    else:
        # Handle any other status codes
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None
    
    # Return the dictionary with emotion scores and dominant emotion
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
