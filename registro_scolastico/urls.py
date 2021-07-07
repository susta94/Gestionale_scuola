from django.urls import path
from registro_scolastico import views

urlpatterns = [
    path('', views.index, name='index'),
    path('studenti', views.studenti, name='studenti'),
    path('professori', views.professori, name='professori'),
    path('qs', views.mostra_qs, name='mostra_qs'),
    path('studente/<id_studente>', views.dettaglio_studente, name='mostra_studente'),
    path('materia/<nome_materia>', views.dettaglio_materia, name='mostra_materia'),
    path('professore/<id_professore>', views.dettaglio_professore, name='mostra_professore'),
]
