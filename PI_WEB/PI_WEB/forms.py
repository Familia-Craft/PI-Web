from django.forms import ModelForm
from PI_WEB.models import Servidor, Ferramenta
from django.db import models
from django import forms 
from django.contrib.auth.hashers import make_password

class LoginForm(forms.Form):
    ra = forms.CharField(max_length=15)
    senha = forms.CharField(widget=forms.PasswordInput)


class ServidorForm(ModelForm):
    class Meta:
        model = Servidor
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput()
        }
    
class FerramentaForm(ModelForm):
    class Meta:
        model = Ferramenta
        fields = '__all__'
        widgets = {
            'descricao': forms.Textarea()
        }






