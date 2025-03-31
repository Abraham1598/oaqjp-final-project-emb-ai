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
    
    # Imprimir la respuesta para depurar
    print(json.dumps(formatted_response, indent=2))
    
    # Asumiendo que la estructura de la respuesta tiene una clave 'document_tone' que contiene un array de tonos
    if 'document_tone' in formatted_response:
        tones = formatted_response['document_tone']['tones']
        emotions = {tone['tone_name'].lower(): tone['score'] for tone in tones}
        
        # Devolviendo un diccionario que contiene los resultados del análisis de sentimientos
        return {
            'anger': emotions.get('anger', 0),
            'disgust': emotions.get('disgust', 0),
            'fear': emotions.get('fear', 0),
            'joy': emotions.get('joy', 0),
            'sadness': emotions.get('sadness', 0),
            'dominant_emotion': max(emotions, key=emotions.get) if emotions else 'none'
        }
    else:
        return {'error': 'No se encontraron emociones en la respuesta.'}
 