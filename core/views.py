
from django.shortcuts import render
from .forms import PeliculaForm, DirectorForm, GeneroForm, BuscarPeliculaForm
from .models import Pelicula

def home(request):
    return render(request, 'core/home.html')

def insertar_pelicula(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PeliculaForm()
    return render(request, 'core/formulario.html', {'form': form, 'titulo': 'Agregar Película'})

def insertar_director(request):
    if request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = DirectorForm()
    return render(request, 'core/formulario.html', {'form': form, 'titulo': 'Agregar Director'})

def insertar_genero(request):
    if request.method == 'POST':
        form = GeneroForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = GeneroForm()
    return render(request, 'core/formulario.html', {'form': form, 'titulo': 'Agregar Género'})

def buscar_pelicula(request):
    resultados = []
    if request.method == 'POST':
        form = BuscarPeliculaForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            resultados = Pelicula.objects.filter(titulo__icontains=titulo)
    else:
        form = BuscarPeliculaForm()
    return render(request, 'core/buscar.html', {'form': form, 'resultados': resultados})
