from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from registro_scolastico.models import *
import random

def index(request):
    return render(request, 'home.html' )


def studenti(request):
    studs = Studente.objects.all()
    context = {'studs': studs}
    return render(request, 'studenti.html', context)

def professori(request):
    profs = Professore.objects.all()
    context = {'profs': profs}
    return render(request, 'professori.html', context)

def mostra_qs(request):
    s = Studente.objects.filter(competenze=Materia.objects.get(nome='italiano'),
                                          classe__in=Aula.objects.filter(anno=3))
    context = {'s': s}
    return render(request, 'qs.html', context)