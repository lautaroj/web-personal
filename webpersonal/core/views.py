from django.shortcuts import render
from django.shortcuts import render, HttpResponse


html_base = """
    <h1>Mi Web Personal</h1>
    <ul>
        <li><a href="/">Portada</a></li>
        <li><a href="/about/">Acerca de</a></li>
        <li><a href="/portafolio/">Portafolio</a></li>
        <li><a href="/contacto/">Contacto</a></li>
    </ul>
"""


def home(request):
    return render(request, "core/home.html")


def about(request):
    return render(request, "core/about.html")


def portafolio(request):
    return render(request, "core/portafolio.html")


def contacto(request):
    return render(request, "core/contacto.html")
