from django import forms


class MyFirstForm(forms.Form):
    nome = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    cognome = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
