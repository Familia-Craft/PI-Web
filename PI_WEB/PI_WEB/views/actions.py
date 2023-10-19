from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpRequest
from PI_WEB.models import Ferramenta, Reserva, Servidor, Usuario, Emprestimo
from PI_WEB.forms import FerramentaForm

@login_required
def ferramenta(request: HttpRequest, id: int):
    f = get_object_or_404(Ferramenta, pk=id)
    
    if request.method == 'POST':
        user = request.user
        usuario = Usuario.objects.get(user=user)
        servidor = Servidor.objects.get(usuario_ptr=usuario)

        reserva = Reserva(ferramenta=f, servidor=servidor)

        reserva.save()
        return redirect('home-page')
    
    context = {'ferramenta': f}
    return render(request, 'ferramenta.html', context)

@permission_required("PI_WEB.add_ferramenta")
def cadastrar_ferramenta(request: HttpRequest):
    frm = FerramentaForm(request.POST or None, request.FILES)
    if frm.is_valid():
        f = frm.save()
        return redirect('ferramenta-page', id=f.id)

    context = {'form': frm}
    return render(request, 'cadastrar_ferramenta.html', context)
    
@permission_required("PI_WEB.add_emprestimo")
def fluxo(request: HttpRequest):
    reservas = Reserva.objects.all()
    emprestimos = Emprestimo.objects.all()
    print(reservas)
    context = {"reservas": reservas, "emprestimos": emprestimos}

    return render(request, "fluxo.html", context)


