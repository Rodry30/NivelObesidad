

import google.generativeai as genai

# Configura tu clave de API
genai.configure(api_key="AIzaSyBVLlmHeluomYwisKyhghvSADLgMdGgTIo")

# Crea el modelo correctamente (sin "models/")
modelo = genai.GenerativeModel("gemini-1.5-flash")

def enviar_mensaje(prompt, historial=None):
    if historial is None:
        historial = []

    chat = modelo.start_chat(history=historial)
    respuesta = chat.send_message(prompt)

    # No necesitas guardar historial si no quieres conversación continua
    return respuesta.text, []
