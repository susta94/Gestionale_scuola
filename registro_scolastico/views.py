from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db.models import ObjectDoesNotExist
from registro_scolastico.models import *
from registro_scolastico.forms import *
import pprint
from django.core.paginator import Paginator
from registro_scolastico.forms import RicercaStudente
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.urls import reverse_lazy
pp = pprint.PrettyPrinter(indent=4)


class LamiaClassView(ListView):
    queryset = Studente.objects.all().only("nome","cognome","email").prefetch_related("competenze")
    template_name = "test_class_views.html"
    paginate_by = 50

class ListaClasse(ListView):
    queryset = Aula.objects.all()
    template_name = "lista_classi.html"
    paginate_by = 50

class IlmioDettaglio(DetailView):
    model = Studente
    template_name = "class_based_detail.html"

class CreateStudent(CreateView):
    model = Studente
    template_name = "class_based_create.html"
    form_class = StudentForm

class UpdateStudent(UpdateView):
    model = Studente
    form_class = StudentForm
    success_url = reverse_lazy("index")

class DettaglioClasse(DetailView):
    model = Aula

# homepage
def index(request):
    return render(request, 'home.html')


# Sezione studenti
def infostudenti(request):
    return render(request, "pagina_studenti.html")


def studenti(request):
    studs = Studente.objects.all()
    context = {'studs': studs}
    paginator = Paginator(studs, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context.update({'paginazione': page_obj})
    return render(request, 'studenti.html', context)


def elimina_studente(request, id_studente):
    studente = Studente.objects.get(id=id_studente)
    studente.delete()
    return render(request, "system_studenti.html")


def ricerca_studente(request):
    context = {"ricerca": RicercaStudente}
    if request.POST:
        dati = dict(request.POST)
        studente = Studente.objects.get(cognome__iexact=dati["cognome"])
        context["studente"] = studente
    return render(request, "ricerca_studente.html", context)


def dettaglio_studente(request, id_studente):
    context = {'stud': Studente.objects.get(id=id_studente)}
    return render(request, 'dettaglio_studente.html', context)


# Sezione professori
def infodocenti(request):
    return render(request, "pagina_docenti.html")


def professori(request):
    profs = Professore.objects.all()
    context = {'profs': profs}
    return render(request, 'professori.html', context)


def dettaglio_materia(request, nome_materia: str):
    nm = '??'
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


def iscrizionestudente(request):
    context = {"iscr_stud": StudentForm}
    if request.POST:
        dati = dict(request.POST)
        iscrizione = Studente.objects.create(nome=dati["nome"][0], cognome=dati["cognome"][0], email=dati["email"][0])
        for materia_id in dati["competenze"]:
            k = Materia.objects.get(pk=int(materia_id))
            iscrizione.competenze.add(k)
        iscrizione.save()
        context["new_stud"] = iscrizione
    return render(request, "iscrizione_studente.html", context)


def elimina_prof(request, ilprof):
    prof = Professore.objects.get(id=ilprof)
    prof.delete()
    context = {"err": f"il professore {prof.nome} {prof.cognome} ?? stato eliminato"}
    return render(request, 'errore.html', context)
