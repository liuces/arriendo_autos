from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'index.html')

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