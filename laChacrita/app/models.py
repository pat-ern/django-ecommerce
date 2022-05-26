from enum import unique
from django.db import models

# Create your models here.

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="Id categoria")
    nombreCategoria = models.CharField(max_length=50, verbose_name="Nombre de categoria")

    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField(null=True)
    descripcion = models.TextField(max_length=500)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombre
    
class Persona(models.Model):
    rut = models.IntegerField(primary_key=True)
    dv = models.CharField(max_length=1, unique=True) #  no deja que sean dos pimary key
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    fechaNacimiento = models.DateField()
    # UniqueConstraint()
    

    def __str__(self):
        return self.nombre