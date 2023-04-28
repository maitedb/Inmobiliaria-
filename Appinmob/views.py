from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from Appinmob.models import *
from Appinmob.forms import *

# Create your views here.

def indexx(request):
    return render(request, 'Appinmob/index.html')

def inquilinos(request):

    inquilinosx = Inquilinos.objects.all()

    return render(request, 'Appinmob/inquilinos.html', {"inquilinos" : inquilinosx } )
def agregar_inquilinos(request):
    if request.method == "POST":
        inquilino_form = InquilinoForm(request.POST)
        if inquilino_form.is_valid():
            data = inquilino_form.cleaned_data
            inquilino = Inquilinos(nombre=data["nombre"],apellido=data["apellido"], correo=data["correo"], telefono =data["telefono"])
            inquilino.save()
            return render(request, 'Appinmob/inquilinos.html')
    else:
        inquilino_form = InquilinoForm()
    return render(request, 'Appinmob/agregar_inquilino.html', {"form": inquilino_form})
def editar_inquilino(request, id_inquilino):
        
    inquilino = Inquilinos.objects.get(id= id_inquilino)

    if request.method == "POST":
        inquilino_form = InquilinoForm(request.POST)
        if inquilino_form.is_valid(): 
                data = inquilino_form.cleaned_data
                inquilino.nombre = data["nombre"]
                inquilino.apellido= data["apellido"]
                inquilino.correo= data["correo"]
                inquilino.telefono= data["telefono"]
                inquilino.save()
                return render(request, 'Appinmob/inquilinos.html')
    else: 
        inquilino_form = InquilinoForm(initial= {'nombre' : inquilino.nombre, 'apellido' : inquilino.apellido, 'correo': inquilino.correo, 'telefono' : inquilino.telefono})
        return render(request, 'appinmob/editar_elemento.html', {'form' : inquilino_form },)
def eliminar_inquilino(request, id_inquilino):

    inquilino = Inquilinos.objects.get(id=id_inquilino)
    nombre = inquilino.nombre
    inquilino.delete()


    return render(request, 'Appinmob/eliminar_elemento.html', {"elemento_eliminado" : nombre, })

def propietarios(request):

    propietariosx = Propietarios.objects.all()

    return render(request, 'Appinmob/propietarios.html', {"propietarios" : propietariosx } )
def cargar_propietario(request):
    if request.method == "POST":

        propform = PropietarioForm(request.POST)
        print(propform)

        if propform.is_valid():
            data = propform.cleaned_data
            
            propietario = Propietarios(nombre=data["nombre"], apellido = data["apellido"], telefono = data["telefono"],correo = data["correo"], CodigoDePropiedad =data["CodigoDePropiedad"])
            propietario.save()
            return render(request, "Appinmob/propietarios.html")
    else:
        propform = PropietarioForm()

    return render(request, "Appinmob/guardar_propietario.html", {"miFormulario": propform})
def buscar_propietario(request):
    if request.method == "POST":

        print(f"\nESTA ES LA INFO: {request.POST['CodigoDePropiedad']}\n")
        codigos = Propietarios.objects.filter(CodigoDePropiedad=int(request.POST["CodigoDePropiedad"]))

        return render(request, "Appinmob/buscar_propietario.html", {'data': [codigos]})
    else:
        miFormulario = PropietarioForm()

    return render(request, "Appinmob/buscar_propietario.html", {"miFormulario": miFormulario})
def eliminar_propietario(request, id_propietario):

    propietario = Propietarios.objects.get(id=id_propietario)
    nombre= propietario.nombre
    propietario.delete()


    return render (request, 'Appinmob/eliminar_elemento.html', {'elemento_eliminado' : nombre})
def editar_propietario(request, id_propietario):
        
    propietario = Propietarios.objects.get(id= id_propietario)

    if request.method == "POST":
        propform= PropietarioForm(request.POST)
        if propform.is_valid(): 
                data = propform.cleaned_data
                propietario.nombre = data["nombre"]
                propietario.apellido= data["apellido"]
                propietario.correo= data["correo"]
                propietario.telefono= data["telefono"]
                propietario.CodigoDePropiedad = data["CodigoDePropiedad"]
                propietario.save()
                return render(request, 'Appinmob/propietarios.html')
    else: 
        propform = PropietarioForm(initial= {'nombre' : propietario.nombre, 'apellido' : propietario.apellido, 'correo': propietario.correo, 'telefono' : propietario.telefono, "CodigoDePropiedad" : propietario.CodigoDePropiedad})
        return render(request, 'appinmob/editar_elemento.html', {'form' : propform },)

def propiedades(request):

    propiedadesx = Propiedades.objects.all()

    return render(request, 'Appinmob/propiedades.html', {"propiedades": propiedadesx})

def leerprop(request, id_propiedad):
    propiedad = get_object_or_404(Propiedades, id=id_propiedad)
    return render(request, 'appinmob/leermas.html', {'propiedad': propiedad})

def cargar_propiedades(request):
        
    if request.method == "POST":
        propiedadesform = PropiedadForm(request.POST)
        if propiedadesform.is_valid():
            data = propiedadesform.cleaned_data

            propiedades = Propiedades(inmueble=data["inmueble"], ambientes = data["ambientes"], contrato = data["contrato"],ubicacion = data["ubicacion"], propietario =data["propietario"], m2 = data['m2'], estado=  data['estado'], imagen=  data['imagen'], empleadoencargado= data['empleadoencargado'], fecha=  data['fecha'])
            propiedades.save()
            return render(request, "Appinmob/propiedades.html")
    else:
        propiedadesform = PropiedadForm()

    return render(request, "Appinmob/guardar_propiedades.html", {"miFormulario": propiedadesform})


