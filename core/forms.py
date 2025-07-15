
from django import forms
from .models import Pelicula, Director, Genero

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = '__all__'

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = '__all__'

class BuscarPeliculaForm(forms.Form):
    titulo = forms.CharField(label='Buscar película')
