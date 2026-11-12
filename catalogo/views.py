# Parte de Gago
from django.shortcuts import render
from django.views.generic import ListView
from .models import Producto

# VISTA BASADA EN FUNCIÓN (FBV)
def home(request):
    # TODO: Retornar render de 'home.html' con contexto básico
    pass

# VISTA BASADA EN CLASE (CBV)
class ProductoListView(ListView):
    model = Producto
    # TODO: Definir template_name, context_object_name, y ordenar queryset por precio
    # Ejemplo: queryset = Producto.objects.filter(stock__gt=0).order_by('precio')