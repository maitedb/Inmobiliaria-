from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'Appinmob/index.html')

def inquilinos(request):
    return render(request, 'Appinmob/inquilinos.html')

def propietarios(request):
    return render(request, 'Appinmob/propietarios.html')

def propiedades(request):
    return render(request, 'Appinmob/propiedades.html')

def empleados(request):
    return render(request, 'Appinmob/empleados.html')