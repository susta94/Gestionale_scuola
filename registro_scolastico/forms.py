from django import forms
from registro_scolastico.models import *


class MyFirstForm(forms.Form):
    nome = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    cognome = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))


class StudentForm(forms.Form):
    nome = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    cognome = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    competenze = forms.ModelMultipleChoiceField(queryset=Materia.objects.all(), widget=forms.SelectMultiple(attrs={"class": "form-control"}))

class RicercaStudente(forms.Form):
    cognome = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
