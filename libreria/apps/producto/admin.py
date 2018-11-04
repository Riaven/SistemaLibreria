from django.contrib import admin
from apps.producto.models import Tipo, Producto

# Register your models here.


admin.site.register(Tipo)
admin.site.register(Producto)