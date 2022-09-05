from django.urls import path
from app_movies import views
from app_movies.views import listar_titulos


urlpatterns = [
    path('', listar_titulos, name="movies"),
    path('crear-titulo/', views.formulario_titulo, name = "formulario_titulo"),
]