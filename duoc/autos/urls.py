from django.urls import path

from .views import inicio, coche1, coche2, coche3, coche4, login, registro, modificar, recuperar, gracias

urlpatterns = [
    path('coches_santiago', inicio, name='inicio'),
    path('coches_santiago/camioneta', coche1, name='coche1'),
    path('coches_santiago/hyundai_accent_mt', coche2, name='coche2'),
    path('coches_santiago/hyundai_staria', coche3, name='coche3'),
    path('coches_santiago/peugeot_traveller', coche4, name='coche4'),
    path('coches_santiago/inicio_sesion', login, name='login'),
    path('coches_santiago/registrarse', registro, name='registro'),
    path('coches_santiago/modificar_cuenta', modificar, name='modificar'),
    path('coches_santiago/recuperar_contrasena', recuperar, name='recuperar'),
    path('coches_santiago/agradecimiento', gracias, name='gracias'),
]