Proyecto Django: Gestor de Películas

Este es un proyecto web desarrollado con Django siguiendo el patrón MVT.  
Permite registrar y buscar información sobre películas, directores y géneros.


Funcionalidades principales

Herencia de HTML usando `base.html`
Tres modelos en `models.py`: `Genero`, `Director`, `Pelicula`
Formularios de alta para insertar datos en cada modelo
Formulario de búsqueda de películas por título
Subido a GitHub y probado desde Colab con ngrok


Estructura del proyecto:

miweb/
├── core/
│   ├── models.py        # Modelos: Genero, Director, Pelicula
│   ├── forms.py         # Formularios para los modelos
│   ├── views.py         # Vistas para insertar y buscar
│   ├── urls.py          # Rutas internas de la app
│   └── templates/
│       └── core/
│           ├── base.html
│           ├── home.html
│           ├── insertar_genero.html
│           ├── insertar_director.html
│           ├── insertar_pelicula.html
│           └── buscar_pelicula.html
├── manage.py


 ¿Cómo probarlo?

Orden sugerido para usar la app:

1 Acceder a `/` para ver la página de inicio.
2 Ir a `/insertar/genero/` y agregar uno o más géneros.
3 Ir a `/insertar/director/` y agregar uno o más directores.
4 Ir a `/insertar/pelicula/` y agregar una película eligiendo género y director.
5 Ir a `/buscar/` para buscar una película por su título.


¿Cómo ejecutarlo en Google Colab?

1. Cloná el repo o copiá los archivos en Colab.
2. Ejecutá las migraciones: 

```bash
!python manage.py makemigrations
!python manage.py migrate

from pyngrok import ngrok
public_url = ngrok.connect(8000)
print(public_url

!python manage.py runserver 0.0.0.0:8000

Entrar al link publico.
