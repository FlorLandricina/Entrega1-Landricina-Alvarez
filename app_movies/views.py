from django.shortcuts import render
from django.template import Template, Context, loader
from app_movies.models import Titulo
from app_movies.models import Genero, Rating

def listar_titulos(request):
    listar_titulos = Titulo.objects.all()
    print(listar_titulos)

    return render(request,"titulos_list.html",{"titulo":listar_titulos})