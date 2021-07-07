from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from registro_scolastico.models import *
from django.db.models import ObjectDoesNotExist
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

def dettaglio_studente(request, id_studente:str):
    stud = Studente.objects.none()
    if id_studente.isdigit():
        stud = Studente.objects.get(id=id_studente)
    elif id_studente.isalpha():
        stud = Studente.objects.filter(nome__icontains=id_studente)
    context = {'stud': stud}
    return render(request, 'dettaglio_stud.html', context)


def dettaglio_materia(request, nome_materia:str):
    nm='ì'
    try:
        nm = Materia.objects.get(nome__iexact=nome_materia)
    except ObjectDoesNotExist:
        context = {'err': "Nessun oggetto trovato con questo nome"}
        return render(request, 'errore.html', context)
    if nm:
        context = {"mat":nm}
        return render(request, 'dettaglio_materia.html', context)
    else:
        context = {'err': "Studente non trovato"}
        return render(request, 'errore.html', context)








def mostra_qs(request):
    s = Studente.objects.filter(competenze=Materia.objects.get(nome='italiano'),
                                          classe__in=Aula.objects.filter(anno=3))
    context = {'s': s}
    return render(request, 'qs.html', context)