from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from Appinmob.views import inquilinos, propietarios, propiedades 
from .forms import CustomUserCreationForm, UserEditForm 
from django.contrib.auth import authenticate, logout,login 
from django.core.cache import cache


@login_required
def mostrarpostlogueo1(request):
    return propietarios(request)

@login_required
def mostrarpostlogueo2(request):
    return inquilinos(request)

@login_required
def mostrarpostlogueo3(request):
    return propiedades(request)

def exit(request):
    logout(request)
    return redirect('index')

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == "POST":
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username= user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data["password1"])
            login(request, user)
        return redirect('index')
    
    return render(request, 'registration/register.html', data)

def perfil(request):
   
   usuario = request.user
   return render(request, "perfil/perfiles.html", {'usuario': usuario})


def editar_perfil(request):
    usuario = request.user

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST, request.FILES, instance=usuario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.username = informacion['username']
            usuario.email = informacion['email']
            usuario.set_password(informacion['password1'])
            usuario.name = informacion['first_name']
            usuario.save()
            cache.delete('user_{}'.format(request.user.pk))

            return render(request, 'Appinmob/index.html')
    else:
        miFormulario = UserEditForm(instance=usuario)

    return render(request, "perfil/editar_perfil.html", {"miFormulario": miFormulario, "usuario": usuario})