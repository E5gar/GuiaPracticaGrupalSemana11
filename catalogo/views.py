# Parte de Gago
from django.shortcuts import render
from django.views.generic import ListView
from .models import Producto


def home(request):
    disponibles = Producto.objects.filter(stock__gt=0)
    contexto = {
        'destacados': disponibles.order_by('-creado_en')[:4],
        'total_productos': Producto.objects.count(),
        'total_disponibles': disponibles.count(),
        'total_categorias': Producto.objects.order_by().values('categoria').distinct().count(),
    }
    return render(request, 'home.html', contexto)


class ProductoListView(ListView):
    model = Producto
    template_name = 'catalogo.html'
    context_object_name = 'productos'

    def get_queryset(self):
        queryset = Producto.objects.order_by('precio')
        categoria = self.request.GET.get('categoria')
        if categoria:
            queryset = queryset.filter(categoria=categoria)
        return queryset

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['categorias'] = (
            Producto.objects.order_by('categoria')
            .values_list('categoria', flat=True)
            .distinct()
        )
        contexto['categoria_activa'] = self.request.GET.get('categoria', '')
        return contexto