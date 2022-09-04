from django.urls import path
from app_movies.views import listar_titulos


urlpatterns = [
    path('', listar_titulos, name="movies")
]