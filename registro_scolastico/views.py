from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from registro_scolastico.models import *
import random

def index(request):
    return render(request, 'home.html' )


def info(request):
    return render(request, 'info.html')