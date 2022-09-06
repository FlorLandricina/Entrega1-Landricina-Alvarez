from django import forms
from . import models


class TituloFormulario (forms.Form):
    nombre = forms.CharField(max_length=150)
    ano_lanzamiento = forms.DateField()
    rating = forms.ModelMultipleChoiceField(queryset=models.Rating.objects.all(), widget=forms.CheckboxSelectMultiple)
    genero = forms.ModelMultipleChoiceField(queryset=models.Genero.objects.all(), widget=forms.CheckboxSelectMultiple)