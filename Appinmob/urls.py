from django.contrib import admin 
from django.urls import path
from Appinmob.views import Inquilino, Indexx, Propietario, Propiedades, Empleado, guardar_form, buscar_propietario, guardar_inquilino

urlpatterns = [
    path('', Indexx, name="index"),
    path('inquilinos/', Inquilino, name="inquilinos"),
    path('propietarios/', Propietario, name="propietarios"),
    path('propiedades/', Propiedades, name="propiedades"),
    path('empleados/', Empleado, name="empleados"),
    path('guardar-inquilino/', guardar_inquilino, name= 'guardar_inquilino'),
    path('guardar-form/', guardar_form, name= 'guardar_form'), 
    path('buscar-propietario/', buscar_propietario, name='buscar_propietario'), 
    
]

