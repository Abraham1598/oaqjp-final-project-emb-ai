import requests
import json


def emotion_detector(text_to_analyse):
    # URL del servicio de análisis de sentimientos
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    
    # Construyendo la carga útil de la solicitud en el formato esperado
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    
    # Encabezado personalizado que especifica el ID del modelo para el servicio de análisis de sentimientos
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    
    # Enviando una solicitud POST a la API de análisis de sentimientos
    response = requests.post(url, json=myobj, headers=header)
    
    
    # Analizando la respuesta JSON de la API
    formatted_response = json.loads(response.text)
    
    
    # Extrayendo la etiqueta de sentimiento y la puntuación de la respuesta
    anger_score = formatted_response['name of the dominant emotion']['anger']
    disgust_score = formatted_response['name of the dominant emotion']['disgust']
    fear_score = formatted_response['name of the dominant emotion']['fear']
    joy_score = formatted_response['name of the dominant emotion']['joy']
    sadness_score = formatted_response['name of the dominant emotion']['sadness']
    
    # Devolviendo un diccionario que contiene los resultados del análisis de sentimientos
    return {'anger': anger_score,'disgust': disgust_score,'fear': fear_score,'joy': joy_score,'sadness': sadness_score,'dominant_emotion': '<name of the dominant emotion>'}
 