from django.shortcuts import render, redirect
from PI_WEB.forms import LoginForm, ServidorForm
from django.http import HttpRequest
from django.contrib import auth


def login(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect('home-page')

    frm = LoginForm(request.POST or None)
    if frm.is_valid():
        servidor = auth.authenticate(request, ra=frm.cleaned_data['ra'], password=frm.cleaned_data['senha'])
        if servidor is not None:

            auth.login(request, servidor)
            return redirect('home-page')
        else:
            frm.add_error(None, 'Usuário ou senha inválidos')

    context = {'form': frm}
    return render(request, "login.html", context)

def cadastro(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect('home-page')
    
    frm = ServidorForm(request.POST or None)
    
    if frm.is_valid():
        servidor = frm.save()
        auth.login(request, servidor)
        redirect("home-page")

    context = {'form': frm}
    return render(request, "cadastro.html", context)

def deslogar(request: HttpRequest):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect("login-page")
    else:
        return redirect("home-page")