from django.urls import path
from registro_scolastico import views

urlpatterns = [
    path('', views.index, name='index'),
    path('studenti', views.studenti, name='studenti'),
    path('professori', views.professori, name='professori'),
    path('qs', views.mostra_qs, name='mostra_qs'),
]
