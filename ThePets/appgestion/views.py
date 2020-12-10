from django.shortcuts import render
from appgestion.models import Cliente
from django.http import HttpResponse
from appgestion.models import Mascota
from datetime import datetime

# Create your views here.

def busqueda_cliente(request):
    return render(request,"busqueda_cliente.html")

#Portada
def index(request):
    return render(request,"index.html")

def busqueda_Mascota(request):
    return render(request,"busqueda_Mascota.html")

def ingreso_cliente(request):
    return render(request,"ingreso_cliente.html")

def ingreso_mascota(request):
    return render(request,"ingreso_mascota.html")

def buscarcliente(request):
    if request.GET['txt_nombre_cliente']:
        cliente_recibido=request.GET['txt_nombre_cliente']
        clientes=Cliente.objects.filter(nombre__icontains=cliente_recibido)
        return render(request,"resultado_busqueda_cliente.html",{"clientes":clientes,"cliente_consultado":cliente_recibido})
    else:
        mensaje="Debe ingresar un cliente para buscar"
    return HttpResponse(mensaje)

def buscarMascota(request):
    if request.GET['txt_nombre_mascota']:
        mascota_recibida=request.GET['txt_nombre_mascota']
        mascotas=Mascota.objects.filter(nombreMascota__icontains=mascota_recibida)
        return render(request,"resultado_busqueda_mascota.html",{"mascotas":mascotas,"mascota_consultado":mascota_recibida})
    else:
        mensaje="Debe ingresar un mascota para buscar"
    return HttpResponse(mensaje)

def ingresar_cliente(request):
    nombre=request.GET["txt_nombre_cliente"]
    apellido=request.GET["txt_apellido_cliente"]
    correo=request.GET["txt_correo_cliente"]
    telefono=request.GET["txt_telefono_cliente"]
    fecha=request.GET["txt_fecha_ingreso"]
    nombredeMascota=request.GET["txt_nombre_mascota_cliente"]
    if len(nombre)>0 and len(apellido)>0 and len(correo)>0 and len(telefono)>0 and len(fecha)>0 and len(nombredeMascota)>0:
        cli=Cliente(nombre=nombre,apellido=apellido,correo=correo,telefono=telefono,fecha=fecha,nombredeMascota=nombredeMascota)
        cli.save()
        mensaje="Cliente Guardado."
    else:
        mensaje="Cliente no ingresado. Faltan datos por ingresar"
    return HttpResponse(mensaje)

def ingresar_mascota(request):
    nombreMascota=request.GET["txt_nombre_mascota"]
    tipoMascota=request.GET["txt_tipo_mascota"]
    raza=request.GET["txt_raza_mascota"]
    edad=request.GET["txt_edad_mascota"]
    sexo=request.GET["txt_sexo_mascota"]
    estado=request.GET["txt_estado_mascota"]
    if len(nombreMascota)>0 and len(tipoMascota)>0 and len(raza)>0 and len(edad)>0 and len(sexo)>0 and len(estado)>0:
        mas=Mascota(nombreMascota=nombreMascota,tipoMascota=tipoMascota,raza=raza,edad=edad,sexo=sexo,estado=estado)
        mas.save()
        mensaje="Mascota guardada."
    else:
        mensaje="Mascota no ingresado. Faltan datos por ingresar"
    return HttpResponse(mensaje)

def eliminar_cliente(request):
    if request.GET["txt_id"]:
        id_recibido=request.GET["txt_id"]
        cliente=Cliente.objects.filter(id=id_recibido)
        if cliente:
            cli=Cliente.objects.get(id=id_recibido)
            cli.delete()
            mensaje="Cliente eliminado"
        else:
            mensaje="Cliente no eliminado. No existen clientes con ese id"
    else:
        mensaje="Debe ingresar un cliente"
    return HttpResponse(mensaje)

def eliminar_mascota(request):
    if request.GET["txt_id"]:
        id_recibido=request.GET["txt_id"]
        mascota=Mascota.objects.filter(id=id_recibido)
        if mascota:
            mas=Mascota.objects.get(id=id_recibido)
            mas.delete()
            mensaje="Mascota eliminado"
        else:
            mensaje="Mascota no eliminado. No existen mascotas con ese id"
    else:
        mensaje="Debe ingresar un mascota"
    return HttpResponse(mensaje)