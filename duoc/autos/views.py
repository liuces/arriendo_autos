
from django.contrib import messages
import requests
from django.shortcuts import get_object_or_404, redirect, render
from .models import automovil, UserProfile

# Create your views here.
def inicio(request):
    automoviles = automovil.objects.all()

    context = {'automoviles': automoviles}
    return render(request, 'index.html', context)

def coche1(request):
    return render(request, 'Camioneta.html')

def coche2(request):
    return render(request, 'HyundaiAccentMT.html')

def coche3(request):
    return render(request, 'HyundaiStaria.html')

def coche4(request):
    return render(request, 'PeugeotTraveller.html')

def login(request):
    return render(request, 'login.html')

def registro(request):
    return render(request, 'registro.html')

def modificar(request):
    return render(request, 'modificar_cuenta.html')

def recuperar(request):
    return render(request, 'recuperar_contrasena.html')

def gracias(request):
    return render(request, 'gracias.html')

def crear_automovil(request):
    if request.method == 'POST':
        patente = request.POST.get('patente')
        nombre_automovil = request.POST.get('nombre_automovil')
        descripcion_automovil = request.POST.get('descripcion_automovil')
        precio = request.POST.get('precio')
        imagen = request.FILES.get('imagen')

        automovil.objects.create(
            patente=patente,
            nombre_automovil=nombre_automovil,
            descripcion_automovil=descripcion_automovil,
            precio=precio,
            imagen=imagen
        )
        messages.success(request, 'Automóvil creado correctamente.')
        return redirect("listado_automoviles")
    return render(request, 'crear.html') 

def editar_automovil(request, patente):
    auto = get_object_or_404(automovil, pk=patente)
    if request.method == 'POST':
        auto.patente = request.POST.get('patente')
        auto.nombre_automovil = request.POST.get('nombre_automovil')
        auto.descripcion_automovil = request.POST.get('descripcion_automovil')
        auto.precio = request.POST.get('precio')
        if 'imagen' in request.FILES:
            auto.imagen = request.FILES['imagen']
        auto.save()
        messages.success(request, 'Automóvil actualizado correctamente.')

        return redirect('listado_automoviles')

    return render(request, 'editar.html', {'auto': auto})

def eliminar_automovil(request, patente):
    auto = get_object_or_404(automovil, pk=patente)
    auto.delete()
    messages.success(request, 'Automóvil eliminado correctamente.')

    return redirect('listado_automoviles')

def listado_automoviles(request):
    automoviles = automovil.objects.all()
    context = {
        'automoviles': automoviles
    }
    return render(request, 'listado_automoviles.html', context)

def listado_automoviles_api(request):

    url = "https://carapi.app/api/makes/v2"

    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjYXJhcGkuYXBwIiwic3ViIjoiNDg0MDdkMzMtODNjZC00MWI4LWIxM2ItNmE1NjI0Y2M2Zjc4IiwiYXVkIjoiNDg0MDdkMzMtODNjZC00MWI4LWIxM2ItNmE1NjI0Y2M2Zjc4IiwiZXhwIjoxNzkxODU2MjQwLCJpYXQiOjE3OTEyNTE0NDAsImp0aSI6IjBjMjFmMjM0LWNlMGItNDdjZC04YzUxLTJhOTM1YmQ5NjgyMyIsInVzZXIiOnsic3Vic2NyaXB0aW9ucyI6W10sInJhdGVfbGltaXRfdHlwZSI6ImhhcmQiLCJhZGRvbnMiOnsiYW50aXF1ZV92ZWhpY2xlcyI6ZmFsc2UsImRhdGFfZmVlZCI6ZmFsc2V9fX0.WQLdUDZ4NxUfo5AsU-6Q-PkkC-R9wiVteZE1kd2JgvI"

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }

    respuesta = requests.get(url, headers=headers)

    if respuesta.status_code == 200:
        datos = respuesta.json()

        print(datos)

        return render(request, 'Autos_api.html', {
            'marcas': datos['data']
        })

    return render(request, 'Autos_api.html', {
        'marcas': []
    })