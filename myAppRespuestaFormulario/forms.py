from django import forms

class FormularioContacto(forms.Form):
    
    name = forms.CharField(required=True)
    last = forms.CharField(required=True)
    number = forms.IntegerField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True)