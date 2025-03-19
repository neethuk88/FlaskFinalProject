import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(URL, json = input_json, headers=Headers)  # Send a POST request to the API with the text and headers
   #return response.text
   # status_code = response.status_code

    emotions = {}
    
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotions.items(), key=lambda x: x[1])
    emotions['dominant_emotion'] = dominant_emotion[0]

    return emotions