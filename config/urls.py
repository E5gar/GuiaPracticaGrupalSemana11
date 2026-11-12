# Parte de Gago
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # TODO: Incluir urls de la app 'catalogo' con namespace o prefijo
]