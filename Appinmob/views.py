from django.shortcuts import render
from django.http import HttpResponse
from Appinmob.models import *
from Appinmob.forms import *
# Create your views here.

def indexx(request):
    return render(request, 'Appinmob/index.html')

def inquilinos(request):
    return render(request, 'Appinmob/inquilinos.html')

def propietarios(request):
    return render(request, 'Appinmob/propietarios.html')

def propiedades(request):
    return render(request, 'Appinmob/propiedades.html')

def Empleado(request):
    return render(request, 'Appinmob/empleados.html')

def guardar_inquilino(request):

    if request.method == "POST":

        miFormulario = InquilinoForm(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion= miFormulario.cleaned_data
            print(f"\n{informacion}\n")
            inquilino = Inquilinos(nombre=informacion["nombre"], apellido = informacion["apellido"], correo =informacion["correo"],  telefono = informacion["telefono"])
            inquilino.save()
            return render(request, "Appinmob/inquilinos.html")
    else:
        miFormulario = InquilinoForm()

    return render(request, "Appinmob/guardar_inquilino.html", {"miFormulario": miFormulario})

    
def guardar_propietario(request):
    if request.method == "POST":

        miFormulario = PropietarioForm(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion= miFormulario.cleaned_data
            print(f"\n{informacion}\n")
            propietario = Propietarios(nombre=informacion["nombre"], apellido = informacion["apellido"], telefono = informacion["telefono"], CodigoDePropiedad =informacion["CodigoDePropiedad"])
            propietario.save()
            return render(request, "Appinmob/propietarios.html")
    else:
        miFormulario = PropietarioForm()

    return render(request, "Appinmob/guardar_form.html", {"miFormulario": miFormulario})

def buscar_propietario(request):
    if request.method == "POST":

        print(f"\nESTA ES LA INFO: {request.POST['CodigoDePropiedad']}\n")
        codigos = Propietarios.objects.filter(CodigoDePropiedad=int(request.POST["CodigoDePropiedad"]))

        return render(request, "Appinmob/buscar_propietario.html", {'data': [codigos]})
    else:
        miFormulario = PropietarioForm()

    return render(request, "Appinmob/buscar_propietario.html", {"miFormulario": miFormulario})


