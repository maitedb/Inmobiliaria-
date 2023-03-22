from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return HttpResponse("ESTA ES LA PAGINA DE INICIO")

def index(request):
    return render(request, 'Appinmob/index.html')
