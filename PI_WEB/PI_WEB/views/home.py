from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from PI_WEB.models import Ferramenta

def get_ferramentas():
    ferramentas = [[]]
    objects = Ferramenta.objects.all()
    for index, obj in enumerate(objects, start=1):
        ferramentas[-1].append(obj)

        if index % 4 == 0:
            ferramentas.append([])
    
    return ferramentas


@login_required
def home(request: HttpRequest):
    ferramentas = get_ferramentas()
    
    print(ferramentas)
    context = {'ferramentas': ferramentas}
    return render(request, "home.html", context)
