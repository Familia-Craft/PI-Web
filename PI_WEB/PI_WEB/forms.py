from django.forms import ModelForm
from PI_WEB.models import Servidor, Ferramenta
from django import forms 
from django.contrib.auth.forms import AuthenticationForm, UsernameField

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True}), max_length=15)


class ServidorForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Servidor
        fields = ['ra', 'nome', 'funcao', 'user']

    
class FerramentaForm(ModelForm):
    class Meta:
        model = Ferramenta
        fields = '__all__'
        widgets = {
            'descricao': forms.Textarea()
        }

class FinalizarFerramenta(ModelForm):
    class Meta:
        pass






