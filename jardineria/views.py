from django.shortcuts import render
from .models import Producto

# Create your views here.


def index(request):
    context={}
    return render(request, 'jardineria/index.html', context)

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'jardineria/productos.html', {'productos': productos})

def formulario(request):
    context={}
    return render(request, 'jardineria/formulario.html', context)


