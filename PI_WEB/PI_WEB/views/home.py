from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from PI_WEB.forms import LoginForm, ServidorForm
from django.http import HttpRequest
from django.contrib import auth

@login_required
def home(request: HttpRequest):
    print(request)
    return render(request, "home.html")

