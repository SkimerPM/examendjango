from django.db import models

class Restaurante(models.Model):
    logo = models.ImageField(upload_to='restaurantes/') 
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    horario_apertura = models.TimeField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class Plato(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE) 
    foto = models.ImageField(upload_to='platos/') 
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    tipo_comida = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} ({self.restaurante.nombre})"