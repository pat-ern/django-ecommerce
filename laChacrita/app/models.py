from django.db import models

# Create your models here.

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True)
    nombreCategoria = models.CharField(max_length=50)

    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField
    descripcion = models.CharField(max_length=500)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre