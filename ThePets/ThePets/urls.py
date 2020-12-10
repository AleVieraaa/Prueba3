"""ThePets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appgestion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('busqueda_cliente/',views.busqueda_cliente),
    path('buscarcliente/',views.buscarcliente),
    path('buscarMascota/',views.buscarMascota),
    path('busqueda_Mascota/',views.busqueda_Mascota),
    path('index/',views.index),
    path('ingreso_cliente/',views.ingreso_cliente),
    path('ingresar_cliente/',views.ingresar_cliente),
    path('ingreso_mascota/',views.ingreso_mascota),
    path('ingresar_mascota/',views.ingresar_mascota),
    path('eliminar_cliente/',views.eliminar_cliente),
    path('eliminar_mascota/',views.eliminar_mascota),
]
