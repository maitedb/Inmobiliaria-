from django.contrib import admin 
from django.urls import path
from Appinmob.views import  indexx
from perfil.views import *
from Appinmob.views import agregar_inquilinos, editar_inquilino, eliminar_inquilino, cargar_propietario, eliminar_propietario, editar_propietario, leerprop, cargar_propiedades, sobrenosotros

urlpatterns = [
    path('', indexx, name="index"),
    path('inquilinos/',mostrarpostlogueo2, name="inquilinos"),
    path('propietarios/', mostrarpostlogueo1, name="propietarios"),
    path('propiedades/', mostrarpostlogueo3, name="propiedades"),
    path('agregar_inquilino/', agregar_inquilinos , name= 'agregar_inquilinos'),
    path('agregar_propietario/', cargar_propietario, name = 'agregar_propietario'),
    path('register/', register, name= 'register'),
    path('logout/', exit, name='exit'),
    path('editarinquilino/<int:id_inquilino>/', editar_inquilino, name='editar_inquilino'),
    path('eliminarinquilino/<int:id_inquilino>/',eliminar_inquilino, name='eliminar_inquilino'),
    path('eliminarpropietario/<int:id_propietario>/',eliminar_propietario, name='eliminar_propietario'),
    path('editarpropietario/<int:id_propietario>/', editar_propietario, name='editar_propietario'),
    path('leermas/<int:id_propiedad>/', leerprop, name='leermas'),
    path('perfil/', perfil, name= 'perfil'),
    path('editar_perfil/', editar_perfil, name= 'editar_perfil' ), 
    path('agregar_propiedad/', cargar_propiedades, name = 'agregar_propiedad'),
    path('sobrenosotros/', sobrenosotros, name= 'sobre_nosotros')

    ]
    

    

    






    #path('sobremi/', mostrar_miinfo , name= 'sobremi' ),
    #path('leermas/<int:id_articulo>/', leermas, name='leermas'),
    #path('perfiles/', perfiles, name='perfiles'))