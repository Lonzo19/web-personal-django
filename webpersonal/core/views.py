from django.shortcuts import render

html_base = """
    <h1>Mi web Personal</h1>
    <ul>
        <li><a href="/">Inicio</a></li>
        <li><a href="/about/">Acerca de</a></li>
        <li><a href="/portfolio/">Vinos</a></li>
        <li><a href="/contact/">Contacto</a></li>
    </ul>
"""

# Create your views here.
def home(request): 
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")
               
def contact(request):
    return render(request, "core/contact.html")

def pago(request): 
    return render(request, "core/pago.html")


    