# blog/urls.py


from django.urls import path
from . import views


urlpatterns = [
    path('formulario/', views.formPrediccion, name='formPrediccion'),
    path('enviar-correo/', views.enviar_correo, name='enviar_correo'),
    path('chat/', views.chat, name='chat')
]
