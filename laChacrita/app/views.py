from errno import EADDRNOTAVAIL
from django.shortcuts import render
from .models import Producto

# INDEX

desc = "Lobularia maritima, commonly called sweet alyssum, is one of the easiest annuals to grow. It is a mat-forming plant that produces spreading mounds of well-branched stems clad with linear, lance-shaped, gray-green leaves (to 1” long). Plants typically grow 3-9” tall to 12” wide. Dense clusters of sweetly fragrant, tiny, white 4-petaled flowers cover the foliage mounds from spring to early summer. Flowering is often so profuse as to totally hide the foliage."

producto1 = Producto(1, "Lobularia", 5970, desc)
producto2 = Producto(2, "Tijera Castellari", 40000, desc)
producto3 = Producto(3, "Bay Laurel", 25800, desc)
producto4 = Producto(4, "Jaula Soporte", 20490, desc)
producto5 = Producto(5, "Cesta Gardeners", 30790, desc)
producto6 = Producto(6, "Lavanda Azul", 11290, desc)
producto7 = Producto(7, "Marigold", 8350, desc)
producto8 = Producto(8, "Arbol Durazno", 29900, desc)
producto9 = Producto(9, "Semilla de Zinnia", 9500, desc)

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