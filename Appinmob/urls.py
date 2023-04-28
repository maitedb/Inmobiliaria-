from django.contrib import admin 
from django.urls import path
from Appinmob.views import  indexx, Empleado
from perfil.views import *

urlpatterns = [
    path('', indexx, name="index"),
    path('inquilinos/',mostrarpostlogueo2, name="inquilinos"),
    path('propietarios/', mostrarpostlogueo1, name="propietarios"),
    path('propiedades/', mostrarpostlogueo3, name="propiedades"),
    path('empleados/', Empleado, name="empleados"),
   # path('guardar-inquilino/',agregarpostlogueo, name= 'guardar_inquilino'),
    #path('guardar-form/', mostrarpostlogueo2, name= 'propietarios'), 
    #path('buscar-propietario/', buscarpostlogueo, name='buscar_propietario'), 
    path('register/', register, name= 'register'),
    path('logout/', exit, name='exit'),
    
]



   #( path('editar//<int:id_articulo>/', editar, name='editar'),
   # path('eliminar/<int:id_articulo>/',eliminar, name='eliminar'),



    #path('sobremi/', mostrar_miinfo , name= 'sobremi' ),
    #path('leermas/<int:id_articulo>/', leermas, name='leermas'),
    #path('perfiles/', perfiles, name='perfiles'))