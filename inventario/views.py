from django.shortcuts import render
from django.http import HttpResponse
from .models import Categoria


def index(request):
    return HttpResponse("Hola Mundo")

def contact(request, name):
    return HttpResponse(f"Hola {name}, estás en la sección de contacto.")

def categorias(request):
    filtro_nombre = request.GET.get("nombre")
    items = Categoria.objects.filter(nombre__contains=filtro_nombre)
    return render(request, "categorias.html", {"categorias": items})
