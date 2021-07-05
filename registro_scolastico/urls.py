from django.urls import path
from registro_scolastico import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('info', views.info, name='info'),
]
