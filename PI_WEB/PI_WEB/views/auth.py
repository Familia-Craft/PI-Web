from django.shortcuts import render, redirect
from PI_WEB.forms import LoginForm, ServidorForm
from django.http import HttpRequest
from django.contrib import auth
from django.contrib.auth.models import User


def login(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect('home-page')

    frm = LoginForm(request.POST or None)
    if frm.is_valid():
        user = User.objects.get(pk=frm.cleaned_data['ra'])
        auth.login(request, user)
        return redirect('home-page')


    context = {'form': frm}
    return render(request, "login.html", context)

def cadastro(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect('home-page')
    
    frm = ServidorForm(request.POST or None)
    
    if frm.is_valid():
        dados = frm.cleaned_data
        user = User.objects.create_user(username=dados['ra'], password=dados['password'])
        servidor = frm.save()
        auth.login(request, user)
        redirect("home-page")

    context = {'form': frm}
    return render(request, "cadastro.html", context)

def deslogar(request: HttpRequest):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect("login-page")
    else:
        return redirect("home-page")