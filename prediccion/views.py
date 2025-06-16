from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
import json
import requests
from django.views.decorators.csrf import csrf_exempt
from .gemini_chat import enviar_mensaje
from django.http import JsonResponse
from .gemini_chat import modelo
from django.http import HttpResponse

CATEGORIAS_OBESIDAD = {
    0: "Peso insuficiente",
    1: "Peso normal",
    2: "Sobrepeso nivel I",
    3: "Sobrepeso nivel II",
    4: "Obesidad tipo I",
    5: "Obesidad tipo II",
    6: "Obesidad tipo III"
}

def formPrediccion(request):
    resultado = None
    datos = {}

    if request.method == 'POST':
        campos = [
            'genero', 'edad', 'estatura', 'peso', 'afdeo', 'favc', 'fcvc', 'ncp',
            'caec', 'tabaco', 'ch20', 'scc', 'faf', 'tue', 'calc', 'mtrans'
        ]

        try:
            for campo in campos:
                datos[campo] = float(request.POST.get(campo)) if campo in ['edad', 'estatura', 'peso'] else int(request.POST.get(campo))

            lista = [datos[campo] for campo in campos]

            response = requests.post('https://prediccionobesidad.onrender.com/predict', json={'features': lista})
            if response.status_code == 200:
                valor = response.json().get('prediction', [None])[0]
                resultado = CATEGORIAS_OBESIDAD.get(valor, "Resultado desconocido")
            else:
                resultado = f"Error de API: {response.status_code}"
        except Exception as e:
            resultado = f"Error: {e}"

    return render(request, 'prediccion/prediccionForm.html', {
        'resultado': resultado,
        'datos': datos
    })


def enviar_correo(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        datos_json = request.POST.get('data_formulario')
        resultado = request.POST.get('resultado')

        try:
            datos = json.loads(datos_json)
        except json.JSONDecodeError:
            datos = {}

        mensaje = "Datos del formulario:\n\n"
        for campo, valor in datos.items():
            mensaje += f"{campo}: {valor}\n"
        mensaje += f"\nResultado: {resultado}"

        send_mail(
            'Resultado de Predicción de Obesidad',
            mensaje,
            'no-reply@tusistema.com',
            [email],
            fail_silently=False
        )

        return HttpResponseRedirect(reverse('formPrediccion'))




@csrf_exempt
def chat(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("mensaje", "")
            datos_form = data.get("datosFormulario", {})
            resultado = data.get("resultado", "")
            historial = data.get("historial", [])
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido"}, status=400)

        # Traducir los datos del formulario a descripciones legibles
        datos_traducidos = traducir_datos(datos_form)

        # Construcción del prompt para el asistente
        prompt = (
            "Eres un asistente de salud enfocado en dar recomendaciones breves, claras y prácticas "
            "sobre estilo de vida saludable. Evita mencionar puntuaciones técnicas o códigos como 'caec=2'. "
            "En su lugar, interpreta los datos y ofrece respuestas en lenguaje sencillo. "
            "No uses respuestas largas ni generales. Sé directo, empático y útil.\n\n"
            "Datos del usuario:\n"
        )

        for clave, valor in datos_traducidos.items():
            prompt += f"- {clave.capitalize()}: {valor}\n"

        prompt += f"\nPregunta del usuario: {user_message}\n"
        prompt += "Responde en menos de 100 palabras."

        # Llamada al modelo (por ejemplo, a través de una función propia)
        respuesta, nuevo_historial = enviar_mensaje(prompt, historial=historial)

        return JsonResponse({"respuesta": respuesta, "historial": nuevo_historial})

    return JsonResponse({"error": "Método no permitido"}, status=405)


def traducir_datos(datos):
    traducciones = {
        "genero": {"1": "Masculino", "2": "Femenino"},
        "afdeo": {"1": "Sí", "0": "No"},
        "favc": {"1": "Sí", "0": "No"},
        "fcvc": {"1": "Nunca", "2": "A veces", "3": "Siempre"},
        "ncp": {"1": "1-2 comidas", "2": "Tres comidas", "3": "Más de tres"},
        "caec": {"1": "1-2 veces", "2": "Tres veces", "3": "Más de tres"},
        "tabaco": {"1": "Sí", "0": "No"},
        "ch20": {"1": "Menos de 1L", "2": "1-2L", "3": "Más de 2L"},
        "scc": {"0": "Sí", "1": "No"},
        "faf": {"0": "Nunca", "1": "1-2 días", "2": "2-4 días", "3": "4-5 días"},
        "tue": {"1": "0-2 horas", "2": "3-5 horas", "3": "Más de 5 horas"},
        "calc": {"0": "Nunca", "1": "A veces", "2": "Frecuentemente", "3": "Siempre"},
        "mtrans": {
            "0": "Caminar",
            "1": "Bicicleta",
            "2": "Motocicleta",
            "3": "Transporte público",
            "4": "Automóvil"
        }
    }

    datos_legibles = {}
    for campo, valor in datos.items():
        if campo in traducciones:
            datos_legibles[campo] = traducciones[campo].get(str(valor), str(valor))
        else:
            datos_legibles[campo] = str(valor)

    return datos_legibles