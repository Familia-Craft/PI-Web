from django.http import JsonResponse, HttpRequest, QueryDict
from PI_WEB.models import Ferramenta, Reserva, Emprestimo, Aluno

def data_ferramenta(request: HttpRequest):
    ferramentas = []
    results = []
    if request.method == 'POST':
        dados = request.POST
        if dados.get("tipo") == "":

            results = Ferramenta.objects.filter(nome__icontains=dados.get("pesquisa"))
        else:
            results = Ferramenta.objects.filter(nome__icontains=dados.get("pesquisa"),tipo=dados.get("tipo"))

    else:
        results = Ferramenta.objects.all()
            
    for f in results:        
        ferramentas.append({
            "id": f.id,
            "nome": f.nome,
            "img_url": f.imagem.url
            })
    
    return JsonResponse({"ferramentas": ferramentas})

