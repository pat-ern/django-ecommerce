from errno import EADDRNOTAVAIL
from django.shortcuts import render

# INDEX

desc = "Lobularia maritima, commonly called sweet alyssum, is one of the easiest annuals to grow. It is a mat-forming plant that produces spreading mounds of well-branched stems clad with linear, lance-shaped, gray-green leaves (to 1” long). Plants typically grow 3-9” tall to 12” wide. Dense clusters of sweetly fragrant, tiny, white 4-petaled flowers cover the foliage mounds from spring to early summer. Flowering is often so profuse as to totally hide the foliage."

class Producto:
    def __init__(self, nombre, descripcion, precio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        super().__init__()

producto1 = Producto("Lobularia", desc, 5970)
producto2 = Producto("Tijera Castellari", desc, 40000)
producto3 = Producto("Bay Laurel", desc, 25800)
producto4 = Producto("Jaula Soporte", desc, 20490)
producto5 = Producto("Cesta Gardeners", desc, 30790)
producto6 = Producto("Lavanda Azul", desc, 11290)
producto7 = Producto("Marigold", desc, 8350, )
producto8 = Producto("Arbol Durazno", desc, 29900)
producto9 = Producto("Semilla de Zinnia", desc, 9500)

contexto = {"producto1" : producto1,
            "producto2" : producto2,
            "producto3" : producto3,
            "producto4" : producto4,
            "producto5" : producto5,
            "producto6" : producto6,
            "producto7" : producto7,
            "producto8" : producto8,
            "producto9" : producto9}

def index(request):
    return render(request, 'app/index.html', contexto)

# PRODUCTO
def producto(request):
    return render(request, 'app/producto.html', contexto)

# CONOCENOS
def conocenos(request):
    return render(request, 'app/conocenos.html')

# CONTACTO
def contacto(request):
    return render(request, 'app/contacto.html')

# DONACIONES
def donaciones(request):
    return render(request, 'app/donaciones.html')