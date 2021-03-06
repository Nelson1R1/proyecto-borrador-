from tkinter import CASCADE
from django.db import models

# Create your models here.

class TipoProducto (models.Model):
    tipo =  models.CharField(max_length=30)

    def __str__(self):
        return self.tipo

class Producto (models.Model):
    codigo =  models.IntegerField()
    nombreP =  models.CharField(max_length=30)
    marca =  models.CharField(max_length=30)
    precio =  models.IntegerField()
    stock = models.IntegerField()
    tipo =  models.ForeignKey(TipoProducto, on_delete= models.CASCADE)
    imagen = models.ImageField(upload_to="productos", null=True)
    descripcion = models.CharField(max_length=90)
    fecha_ingreso= models.DateField()

    def __str__(self):
        return self.nombreP

class TipoUsuario (models.Model):
    tipoUser = models.CharField(max_length=15)

    def __str__(self):
        return self.tipoUser

class Usuario (models.Model):
    rut = models.IntegerField()
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    correo = models.CharField(max_length=50)
    fechaN = models.DateField()
    tipo = models.ForeignKey(TipoUsuario, on_delete= models.CASCADE)

    def __str__(self):
        return self.rut

class Carrito (models.Model):
    nombreC =  models.CharField(max_length=30)
    marca =  models.CharField(max_length=30)
    precio =  models.IntegerField()
    tipo =  models.ForeignKey(TipoProducto, on_delete= models.CASCADE)
    codigo = models.ForeignKey(Producto, on_delete= models.CASCADE)

    def __str__(self):
        return self.nombreC

class HistorialCompras (models.Model):
    nombreH = models.CharField(max_length=30)
    marca =  models.CharField(max_length=30)
    precio =  models.IntegerField()
    tipo =  models.ForeignKey(TipoProducto, on_delete= models.CASCADE)
    codigo = models.ForeignKey(Producto, on_delete= models.CASCADE)

    def __str__(self):
        return self.nombreH

