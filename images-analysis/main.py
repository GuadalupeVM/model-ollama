import base64
import requests
import json

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        return encoded_string.decode('utf-8')

while True:
    # Ingresar ruta de la imagen y el prompt manualmente
    ruta_imagen = input("Ingresa la ruta de la imagen (o escribe 'salir' para terminar): ")
    if ruta_imagen.lower() == 'salir':
        break

    prompt = input("Ingresa el prompt: ")

    # Convertir la imagen a base64
    base64_image = image_to_base64(ruta_imagen)
    print("Imagen en Base64: lista")

    # Datos para la solicitud a la API
    data = {
        "model": "llava",
        "prompt": prompt,
        "system": "Responde como si fueras un profesional de artes",
        "stream": False,
        "images": [base64_image]  
    }

    # Realizar solicitud a la API local
    try:
        response = requests.post('http://localhost:11434/api/generate', json=data)
        response.raise_for_status()  # Levantar una excepción para respuestas con errores
        response_data = response.json()
        print(response_data['response'])
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")
