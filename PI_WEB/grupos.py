from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group
from PI_WEB.models import *

bolsistas, created = Group.objects.get_or_create(name='Bolsistas')
aluno = ContentType.objects.get_for_model(Aluno)
emprestimo = ContentType.objects.get_for_model(Emprestimo)
reserva = ContentType.objects.get_for_model(Reserva)
ferramenta = ContentType.objects.get_for_model(Ferramenta)

bolsistas.permissions.add(*Permission.objects.filter(content_type=aluno))
bolsistas.permissions.add(*Permission.objects.filter(content_type=emprestimo))
bolsistas.permissions.add(*Permission.objects.filter(content_type=reserva))
bolsistas.permissions.add(*Permission.objects.filter(content_type=ferramenta))

professores, created = Group.objects.get_or_create(name='Professores')

professores.permissions.add(*Permission.objects.filter(content_type=reserva))
professores.permissions.add(Permission.objects.get(codename="view_ferramenta", content_type=ferramenta))
professores.permissions.add(Permission.objects.get(codename="view_emprestimo", content_type=emprestimo))
professores.permissions.add(Permission.objects.get(codename="view_aluno", content_type=aluno))