from django.db import models
from django.contrib.auth.models import User
from requests import request

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
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    puntuacion = models.IntegerField(choices=opciones_calificacion)
    comentario = models.TextField(max_length=500)
    fecha = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.id) + str(self.idProducto) + str(self.usuario.id) + str(self.puntuacion) + str(self.fecha.strftime("%d%m%y%H%M"))

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
    fecha = models.DateTimeField(auto_now_add = True)
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
    suscriptor = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    fecha = models.DateTimeField(auto_now= True)
    tipo_suscripcion = models.ForeignKey(TipoSuscripcion, on_delete=models.CASCADE)
    recibe_informe = models.BooleanField(default = False, null = True)
    estado = models.BooleanField(default = True, null = True)

    def __str__(self):
        return self.tipo_suscripcion.nombre

#-------------------------------------------------------#

# COMPRA-PRODUCTO

cantidad = ([
    [1,"1"],
    [2,"2"],
    [3,"3"],
    [4,"4"],
    [5,"5"]
])

class DetalleCarrito(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(choices=cantidad)
    comprador = models.ForeignKey(User, on_delete=models.CASCADE)
    subtotal = models.IntegerField(default=0)

    def __str__(self):
        return self.producto.nombre

class Compra(models.Model):
    comprador = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now= True)
    total = models.IntegerField(default=0)
    descuento = models.IntegerField(default=0)
    valor_final = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id) + str(self.comprador.id) + str(self.fecha.strftime("%d%m%y%H%M"))

class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)
    subtotal = models.IntegerField(default=0)

    def __str__(self):
        return str(self.producto.id) + str(self.compra)

class EstadoPedido(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion

class Pedido(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    estado = models.ForeignKey(EstadoPedido, default = 1, on_delete=models.CASCADE)
    actualizacion = models.DateTimeField(null=True)

    def __str__(self):
        return str(self.id) + str(self.compra)