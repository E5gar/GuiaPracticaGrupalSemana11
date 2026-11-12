# Parte de Huamanlazo
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.CharField(max_length=50)
    stock = models.PositiveIntegerField()
    creado_en = models.DateTimeField(auto_now_add=True)
    marca = models.CharField(max_length=50, blank=True)
    descripcion = models.CharField(max_length=200, blank=True)
    imagen_url = models.URLField(max_length=500, blank=True)

    class Meta:
        verbose_name_plural = "Productos"
        ordering = ["-creado_en"]

    def __str__(self):
        return f"{self.marca} {self.nombre}".strip()