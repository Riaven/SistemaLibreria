from django.db import models

# Create your models here.


class Tipo (models.Model):
    nombre = models.CharField(max_length = 50)

    def __str__ (self):
        return '{}'.format(self.nombre)



class Producto(models.Model):
    nombre = models.CharField(max_length = 50) 
    descripcion = models.CharField(max_length = 500) 
    precio = models.CharField(max_length = 50) 
    cantidad = models.CharField(max_length = 50) 
    tipo = models.ForeignKey(Tipo, default=1, on_delete=models.CASCADE)
    codigo = models.CharField(max_length = 50, default=000)
    def __str__(self):
        return '{}'.format(self.nombre)