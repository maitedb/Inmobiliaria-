from django.urls import path
from Appinmob.views import inicio, index

urlpatterns = [
    path('', inicio),
    path('index/', index),
]

