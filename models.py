from tkinter import CASCADE
from django.db import models

# Create your models here.

class TipoProducto (models.Model):
    tipo =  models.CharField(max_length=30)

    def __str__(self):
        return self.tipo

class Producto (models.Model):
    codigo =  models.IntegerField
    nombre =  models.CharField(max_length=30)
    marca =  models.CharField(max_length=30)
    precio =  models.CharField(max_length=30)
    stock = models.IntegerField
    tipo =  models.ForeignKey(TipoProducto, on_delete= models.CASCADE)

    def __str__(self):
        return self.nombre

class TipoUsuario (models.Model):
    tipoUser = models.CharField(max_length=15)

    def __str__(self):
        return self.tipoUser

class Usuario (models.Model):
    rut = models.IntegerField
    nombre = models.CharField
    apellido = models.CharField
    correo = models.CharField
    fechaN = models.DateField
    tipo = models.ForeignKey(TipoUsuario, on_delete= models.CASCADE)

    def __str__(self):
        return self.rut

class Carrito (models.Model):
    nombre =  models.CharField(max_length=30)
    marca =  models.CharField(max_length=30)
    precio =  models.CharField(max_length=30)
    tipo =  models.ForeignKey(TipoProducto, on_delete= models.CASCADE)
    codigo = models.ForeignKey(Producto, on_delete= models.CASCADE)