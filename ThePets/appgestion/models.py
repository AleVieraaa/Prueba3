from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    correo=models.EmailField()
    telefono=models.CharField(max_length=10)
    fecha=models.DateField()
    nombredeMascota=models.CharField(max_length=30)

class Mascota(models.Model):
    nombreMascota=models.CharField(max_length=30)
    tipoMascota=models.CharField(max_length=30)
    raza=models.CharField(max_length=30)
    edad=models.CharField(max_length=30)
    sexo=models.CharField(max_length=10)
    estado=models.CharField(max_length=30)