from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from PI_WEB.models import Ferramenta
@login_required
def home(request: HttpRequest):
    ferramentas = Ferramenta.objects.all()

    context = {'ferramentas': ferramentas}
    return render(request, "home.html", context)
