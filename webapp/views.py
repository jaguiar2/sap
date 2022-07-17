from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from personas.models import Persona, Domicilio


def bienvenido(request):
    no_personas_var = Persona.objects.count()
    # personas = Persona.objects.all() # Querey con el objeto manager
    personas = Persona.objects.order_by('id', 'nombre')  # ordenar de manera ascendente
    return render(request, 'bienvenido.html', {'no_personas': no_personas_var, 'personas': personas})
    # Se debe de crear una carpeta de Templates dentro de webapp


def verDomicilio(request):
    no_domicilios_var = Domicilio.objects.count()
    # domicilios = Domicilio.objects.all()  # Querey con el objeto manager
    domicilios = Domicilio.objects.order_by('-id')  # ordenar de manera descendente
    return render(request, 'personas/domicilio.html', {'no_domicilios': no_domicilios_var, 'domicilios': domicilios})
