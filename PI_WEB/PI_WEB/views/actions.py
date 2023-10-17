from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpRequest
from PI_WEB.models import Ferramenta
from PI_WEB.forms import FerramentaForm

@login_required
def ferramenta(request: HttpRequest, id: int):
    f = get_object_or_404(Ferramenta, pk=id)
    
    context = {'ferramenta': f}
    return render(request, 'ferramenta.html', context)

@permission_required("PI_WEB.add_ferramenta")
def cadastrar_ferramenta(request: HttpRequest):
    frm = FerramentaForm(request.POST or None)
    if frm.is_valid():
        frm.save()
        return redirect('home-page')

    context = {'form': frm}
    return render(request, 'cadastrar_ferramenta.html', context)
    


