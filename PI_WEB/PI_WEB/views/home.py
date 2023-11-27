from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from PI_WEB.models import Ferramenta



@login_required
def home(request: HttpRequest):
    ferramentas = Ferramenta.objects.all()
    r = range(32)
    print(ferramentas)
    context = {'ferramentas': ferramentas, "range": r}
    return render(request, "home.html", context)
