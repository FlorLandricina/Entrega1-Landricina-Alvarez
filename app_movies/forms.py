from django import forms


class TituloFormulario (forms.Form):
    nombre = forms.CharField(max_length=150)
    ano_lanzamiento = forms.DateField()
    rating = forms.CharField(max_length=150)
    genero = forms.CharField(max_length=150)
