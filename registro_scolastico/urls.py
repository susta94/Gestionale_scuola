from django.urls import path
from registro_scolastico import views

urlpatterns = [
    path('', views.index, name='index'),                                                                # Homepage

    path('info_studenti', views.studenti, name='info_studenti'),                                    # Sezione studenti
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


    path('class_test', views.LamiaClassView.as_view(), name="test-classi"),
    path('class_detail/<pk>', views.IlmioDettaglio.as_view(), name="test-dettaglio"),
    path('class_create', views.CreateStudent.as_view(), name="class_create"),
    path('class_update/<pk>', views.UpdateStudent.as_view(), name="class-update"),
    path('class_classe/<pk>', views.DettaglioClasse.as_view(), name="dett-classe"),
    path('lista_classi', views.ListaClasse.as_view(), name="lista-classe"),

]
