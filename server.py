"""
Flask Emotion Detector Web App
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """
    Renderiza la página principal.
    """
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET", "POST"])
def emotion_detector_route():
    """
    Procesa el texto recibido y devuelve las emociones detectadas o un mensaje de error
    si la entrada es inválida.
    """
    text_to_analyze = request.values.get("textToAnalyze")
    result = emotion_detector(text_to_analyze)
    if result.get('dominant_emotion') is None:
        return "¡Texto inválido! ¡Por favor, inténtalo de nuevo!"
    response = (
        "Para la declaración dada, la respuesta del sistema es "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} y "
        f"'sadness': {result['sadness']}. "
        f"La emoción dominante es {result['dominant_emotion']}."
    )
    return response


if __name__ == "__main__":
    app.run(host="localhost", port=5002)
