from django.shortcuts import render, redirect
from PI_WEB.forms import LoginForm, ServidorForm
from django.http import HttpRequest
from django.contrib import auth
from django.contrib.auth.models import User


def login(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect('home-page')

    frm = LoginForm(request, data=request.POST)
    if frm.is_valid():
        auth.login(request, frm.get_user())
        return redirect(request.GET.get('next', 'home-page'))

    context = {'form': frm}
    return render(request, "login.html", context)

def cadastro(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect('home-page')
    
    frm = ServidorForm(request.POST or None)

    if frm.is_valid():
        dados = frm.cleaned_data
        user = User.objects.create_user(username=dados['ra'], password=dados['password'])
        frm.instance.user = user
        frm.save()
        auth.login(request, user)
        return redirect("home-page")

    context = {'form': frm}
    return render(request, "cadastro.html", context)

def deslogar(request: HttpRequest):
    auth.logout(request)
    return redirect('login-page')