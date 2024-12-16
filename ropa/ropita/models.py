from django.db import models

class Stock(models.Model):
    titulo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=100)
    prenda = models.CharField(max_length=100)
    talle = models.CharField(max_length=10, choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')])
    color = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.titulo
