from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpRequest
from PI_WEB.models import Ferramenta, Reserva, Servidor, Usuario, Emprestimo
from PI_WEB.forms import FerramentaForm
from datetime import datetime

def get_servidor(user):
    usuario = Usuario.objects.get(user=user)
    servidor = Servidor.objects.get(usuario_ptr=usuario)

    return servidor
@login_required
def ferramenta(request: HttpRequest, id: int):
    f = get_object_or_404(Ferramenta, pk=id)
    
    if request.method == 'POST':
        user = request.user
        usuario = Usuario.objects.get(user=user)
        servidor = Servidor.objects.get(usuario_ptr=usuario)

        reserva = Reserva(ferramenta=f, servidor=servidor, status="Pendente")

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

    if request.method == "POST":
        if "idReserva" in request.POST.dict().keys():
            idR = request.POST.get('idReserva')
            raS = request.POST.get("idDevolvedor")
            return redirect('validar_emprestimo-page', id=idR, ra=raS)
        raS = request.POST.get("idDevolvedor")
        idEmp = request.POST.get('idEmprestimo')

        usuario = Usuario.objects.get(ra=raS)
        emprestimo = Emprestimo.objects.get(id=idEmp)
        servidor = get_servidor(request.user)

        emprestimo.supervisor_devolucao = servidor
        emprestimo.responsavel_devolucao = usuario
        emprestimo.data_devolucao = datetime.now()
        reserva = emprestimo.reserva
        reserva.status = "Finalizada"
        emprestimo.save()
        reserva.save()




    context = {"reservas": reservas, "emprestimos": emprestimos}

    return render(request, "fluxo.html", context)

@permission_required("PI_WEB.add_emprestimo")
def validar_emprestimo(request, id, ra):

    pegador = Usuario.objects.get(ra=ra)
    reserva = Reserva.objects.get(id=id)
    emprestimo = Emprestimo(usuario=pegador, reserva=reserva)
    emprestimo.save()
    reserva.status = "Em andamento"
    reserva.save()
    
    return redirect("fluxo-page")

@login_required
def meu_fluxo(request):
    servidor = get_servidor(request.user)
    reservas = Reserva.objects.filter(servidor=servidor)
    
    emprestimos = Emprestimo.objects.filter(reserva__in=reservas)
    context = {"reservas": reservas, "emprestimos": emprestimos}


    return render(request, "meu_fluxo.html", context)
