from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from registro_scolastico.models import *
from django.db.models import ObjectDoesNotExist
from registro_scolastico.forms import MyFirstForm
import random
import pprint
pp = pprint.PrettyPrinter(indent=4)


def index(request):
    return render(request, 'home.html')


def studenti(request):
    studs = Studente.objects.all()
    context = {'studs': studs}
    return render(request, 'studenti.html', context)


def professori(request):
    profs = Professore.objects.all()
    context = {'profs': profs}
    return render(request, 'professori.html', context)


def dettaglio_studente(request, id_studente: str):
    stud = Studente.objects.none()
    if id_studente.isdigit():
        stud = Studente.objects.get(id=id_studente)
    elif id_studente.isalpha():
        stud = Studente.objects.filter(nome__icontains=id_studente)
    context = {'stud': stud}
    return render(request, 'dettaglio_stud.html', context)


def dettaglio_materia(request, nome_materia: str):
    nm = 'ì'
    try:
        nm = Materia.objects.get(nome__iexact=nome_materia)
    except ObjectDoesNotExist:
        context = {'err': "Nessun oggetto trovato con questo nome"}
        return render(request, 'errore.html', context)
    if nm:
        context = {"mat": nm}
        return render(request, 'dettaglio_materia.html', context)
    else:
        context = {'err': "Studente non trovato"}
        return render(request, 'errore.html', context)


def mostra_qs(request):
    s = Studente.objects.filter(competenze=Materia.objects.get(nome='italiano'),
                                classe__in=Aula.objects.filter(anno=3))
    context = {'s': s}
    return render(request, 'qs.html', context)


def dettaglio_professore(request, id_professore):
    context = {'prof': Professore.objects.get(id=id_professore)}
    return render(request, 'dettaglio_prof.html', context)


def form_test_view(request):
    context = {"ilmioform": MyFirstForm}
    if request.POST:
        dati = dict(request.POST)
        creasion = Professore.objects.create(nome=dati["nome"][0], cognome=dati["cognome"][0], email=dati["email"][0])
        creasion.save()
        context["new_prof"] = creasion


    return render(request, 'form_test.html', context)


def elimina_prof(request, ilprof):
    prof = Professore.objects.get(id=ilprof)
    prof.delete()
    context = {"err": f"il professore {prof.nome} {prof.cognome} è stato eliminato"}
    return render(request, 'errore.html', context)