from django.urls import path
from registro_scolastico import views

urlpatterns = [
    path('', views.index, name='index'),                                                                # Homepage

    path('info_studenti', views.infostudenti, name='info_studenti'),                                    # Sezione studenti
    path('lista-studenti', views.studenti, name='studenti'),                                            # Lista degli studenti
    path('dettaglio-studente/<id_studente>', views.dettaglio_studente, name='dettaglio_studente'),      # Dettaglio del singolo studente
    path('elimina-studente/<id_studente>', views.elimina_studente, name='elimina_studente'),            # Elimina studente
    path('ricerca-studente', views.ricerca_studente, name='ricerca_studente'),                          # Ricerca studente
    path('iscrizione-studente', views.iscrizionestudente, name='iscrizione_studente'),                  # Iscrizione

    path('info_docenti', views.infodocenti, name='info_docenti'),
    path('professori', views.professori, name='professori'),
    path('elimina_prof/<ilprof>', views.elimina_prof, name='elimina_prof'),
    path('qs', views.mostra_qs, name='mostra_qs'),
    path('materia/<nome_materia>', views.dettaglio_materia, name='mostra_materia'),
    path('professore/<id_professore>', views.dettaglio_professore, name='mostra_professore'),
    path('test_form', views.form_test_view, name='test_form'),
]
