from ast import Return
from django.shortcuts import render
from django.template import Template, Context, loader
from app_movies.models import Titulo
from app_movies.models import Genero, Rating
from app_movies.forms import TituloFormulario


def inicio(request):
    return render(request, "app_movies/inicio.html")


def listar_titulos(request):
    listar_titulos = Titulo.objects.all()
    print(listar_titulos)
    return render(request,"app_movies/titulos_list.html",{"titulo":listar_titulos})


def formulario_titulo(request):
    if request.method == 'POST':
        formulario = TituloFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            titulo = Titulo(nombre=data['nombre'], ano_lanzamiento=data['ano_lanzamiento'], rating=data['rating'], genero= data['genero'] )
            titulo.save()
            return render(request, "app_movies/inicio.html")
    else:
        formulario = TituloFormulario()
    return render(request, "app_movies/form_titulo.html", {'formulario': formulario})

def busqueda_titulo(request):
    return render(request, "app_movies/form_busqueda_titulo.html")


def buscar(request):
    if request.GET["titulo"]:
        titulo = request.GET["titulo"]
        peliculas = Titulo.objects.filter(titulo__icontains=titulo)
        return render(request,"app_movies/titulos_list.html",{"titulo":listar_titulos})
    else:
        return render(request,"app_movies/titulos_list.html",{"titulo":[]})
