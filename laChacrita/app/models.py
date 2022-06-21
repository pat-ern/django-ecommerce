from enum import unique
from tabnanny import verbose
from django.db import models
from django.forms import ValidationError

# USUARIO
class Usuario(models.Model):
    rut = models.IntegerField(primary_key=True)
    dv = models.CharField(max_length=1)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    correo = models.EmailField()
    fechaNacimiento = models.DateField()
    fechaRegistro = models.DateField(auto_now_add = True)

    def __str__(self):
        return (f'{self.nombre} {self.apellido}')

# CATEGORIA PRODUCTO
class CategoriaProducto(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="Id categoria")
    nombreCategoria = models.CharField(max_length=50, verbose_name="Nombre de categoria")

    def __str__(self):
        return self.nombreCategoria

# PRODUCTO
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField(null=True)
    descripcion = models.TextField(max_length=500)
    categoria = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="productos", null=True)
    puntuacion_avg = models.IntegerField(default=True, null=True)
    stock = models.IntegerField(default=1)
    #vendedor = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ('nombre',)

# CALIFICACION 
opciones_calificacion = [
    [1,"1"],
    [2,"2"],
    [3,"3"],
    [4,"4"],
    [5,"5"]
]

class Calificacion(models.Model):
    id = models.AutoField(primary_key=True)
    idProducto = models.IntegerField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    puntuacion = models.IntegerField(choices=opciones_calificacion)
    comentario = models.TextField(max_length=500)
    fecha = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.comentario

# COMPRA-PRODUCTO
class CompraProducto(models.Model):
    idCompra = models.AutoField(primary_key=True)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha = models.DateField()
    cantProductos = models.IntegerField()
    montoTotal = models.IntegerField()
    comprador = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.idCompra

# ASUNTO CONTACTO
class AsuntoContacto(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="Id asunto")
    nombre = models.CharField(max_length=50, verbose_name="Nombre asunto")

    def __str__(self):
        return self.nombre

# CONTACTO
class Contacto(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Id contacto")
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    mensaje = models.TextField(max_length=500)
    checkOfertas = models.BooleanField(verbose_name="Recibir informacion")
    fecha = models.DateField(auto_now_add = True)
    asunto = models.ForeignKey(AsuntoContacto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

# TIPO SUSCRIPCION
class TipoSuscripcion(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="Id tipo de suscripcion")
    nombre = models.CharField(max_length=50, verbose_name="Nombre tipo de suscripcion")
    monto = models.IntegerField(default = 0, verbose_name="Monto de suscripcion")

    def __str__(self):
        return self.nombre

# SUSCRIPCION
class Suscripcion(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Id suscripcion")
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    fecha = models.DateField(auto_now= True)
    telefono = models.IntegerField()
    tipo_suscripcion = models.ForeignKey(TipoSuscripcion, on_delete=models.CASCADE)
    recibe_informe = models.BooleanField(default = False, null = True)
    estado = models.BooleanField(default = True, null = True)

    def __str__(self):
        return self.nombre