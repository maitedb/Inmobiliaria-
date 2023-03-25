from django.urls import path
from Appinmob.views import *

urlpatterns = [
    path('', index, name="index"),
    path('inquilinos/', inquilinos, name="inquilinos"),
    path('propietarios/', propietarios, name="propietarios"),
    path('propiedades/', propiedades, name="propiedades"),
    path('empleados/', empleados, name="empleados"),
]

