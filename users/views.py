from django.shortcuts import render

# Create your views here.
# Create your views here.
from django.http import HttpResponse

def status(request):
    return HttpResponse("Servicio activo", status=200)
