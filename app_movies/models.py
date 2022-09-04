from pickle import TRUE
from django.db import models
from http.client import HTTPResponse
from datetime import date

"""
Proyecto Web Django con patrón MVT que incluya:
1. Herencia de HTML.
2. Por lo menos 3 clases en models.
3. Un formulario para insertar datos a todas las clases de tu models.
3. Un formulario para buscar algo en la BD
4. Readme que indique el orden en el que se prueban las cosas y/o donde están las funcionalidades.
"""
class Titulo(models.Model):
    nombre = models.CharField(max_length=150)
    ano_lanzamiento = models.DateField()
    rating = models.ForeignKey('Rating', on_delete=models.CASCADE, null=True)
    genero = models.ForeignKey('Genero', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.ano_lanzamiento}"

class Rating(models.Model):
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.rating}"

class Genero(models.Model):
    genero = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.genero}"

