from django.urls import path
from . import views
from .views import crear_automovil, eliminar_automovil, inicio, coche1, coche2, coche3, coche4, listado_automoviles, login, registro, modificar, recuperar, gracias, editar_automovil

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
    path('coches_santiago/automovil/<str:patente>/editar/', editar_automovil, name='editar_automovil'),
    path('coches_santiago/automovil/crear', crear_automovil, name='crear_automovil'),
    path('coches_santiago/automovil/listado', listado_automoviles, name='listado_automoviles'),
    path('coches_santiago/automovil/<str:patente>/eliminar/', eliminar_automovil, name='eliminar_automovil'),
]