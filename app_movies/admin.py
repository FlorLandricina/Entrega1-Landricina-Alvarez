from django.contrib import admin
from app_movies.models import Titulo, Genero, Rating

admin.site.register(Titulo)
admin.site.register(Genero)
admin.site.register(Rating)
