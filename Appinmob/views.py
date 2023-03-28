from django.shortcuts import render
from django.http import HttpResponse
from Appinmob.models import *
from Appinmob.forms import Guardar_inquilinoForm

# Create your views here.

def Indexx(request):
    return render(request, 'Appinmob/index.html')

def Inquilino(request):
    return render(request, 'Appinmob/inquilinos.html')

def Propietario(request):
    return render(request, 'Appinmob/propietarios.html')

def Propiedades(request):
    return render(request, 'Appinmob/propiedades.html')

def Empleado(request):
    return render(request, 'Appinmob/empleados.html')

def guardar_inquilino(request):

    if request.method == "POST":
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        correo = request.POST["correo"]
        telefono = request.POST["telefono"]
        inquilino = Inquilinos(nombre=nombre, apellido=apellido, correo=correo, telefono=telefono)
        inquilino.save()
    return render(request, "Appinmob/guardar_inquilino.html")
    
def guardar_form(request):


    if request.method == "POST":

        miFormulario = Guardar_inquilinoForm(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion= miFormulario.cleaned_data
            print(f"\n{informacion}\n")
            inquilino = Inquilinos(nombre=informacion["nombre"], apellido = informacion["apellido"], correo=informacion["correo"], telefono = informacion["telefono"])
            inquilino.save()
            return render(request, "Appinmob/index.html")
    else:
        miFormulario = Guardar_inquilinoForm()

    return render(request, "Appinmob/guardar_form.html", {"miFormulario": miFormulario})

