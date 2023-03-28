from django.shortcuts import render
from django.http import HttpResponse
from Appinmob.models import *
from Appinmob.forms import Guardar_propietarioForm, Guardar_inquilinoForm
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

        miFormulario = Guardar_inquilinoForm(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion= miFormulario.cleaned_data
            print(f"\n{informacion}\n")
            inquilino = Inquilinos(nombre=informacion["nombre"], apellido = informacion["apellido"], correo =informacion["correo"],  telefono = informacion["telefono"])
            inquilino.save()
            return render(request, "Appinmob/inquilinos.html")
    else:
        miFormulario = Guardar_inquilinoForm()

    return render(request, "Appinmob/guardar_inquilino.html", {"miFormulario": miFormulario})



    
def guardar_form(request):
    if request.method == "POST":

        miFormulario = Guardar_propietarioForm(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion= miFormulario.cleaned_data
            print(f"\n{informacion}\n")
            propietario = Propietarios(nombre=informacion["nombre"], apellido = informacion["apellido"], telefono = informacion["telefono"], CodigoDePropiedad =informacion["CodigoDePropiedad"])
            propietario.save()
            return render(request, "Appinmob/propietarios.html")
    else:
        miFormulario = Guardar_propietarioForm()

    return render(request, "Appinmob/guardar_form.html", {"miFormulario": miFormulario})

def buscar_propietario(request):
    if request.method == "POST":

        print(f"\nESTA ES LA INFO: {request.POST['CodigoDePropiedad']}\n")
        codigos = Propietarios.objects.filter(CodigoDePropiedad=int(request.POST["CodigoDePropiedad"]))

        return render(request, "Appinmob/buscar_propietario.html", {'data': [codigos]})
    else:
        miFormulario = Guardar_propietarioForm()

    return render(request, "Appinmob/buscar_propietario.html", {"miFormulario": miFormulario})


