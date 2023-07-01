from django.db import models

class Ferramenta(models.Model):
    nome = models.CharField(max_length=40)
    descricao = models.TextField()
    tipo = models.CharField(max_length=10)
    imagem = models.ImageField(height_field=None, width_field=None, max_length=None)

class Usuario(models.Model):
    ra = models.CharField(max_length=15, primary_key=True)
    nome = models.CharField(max_length=40)
    emprestimos = models.ManyToManyField('Reserva', through='Emprestimo', through_fields=('usuario', 'reserva'))

class Servidor(Usuario):
    funcao = models.CharField(max_length=9)
    ferramentas_reservadas = models.ManyToManyField(Ferramenta, through='Reserva')

class Aluno(Usuario):
    curso = models.CharField(max_length=7)

class Reserva(models.Model):
    ferramenta = models.ForeignKey(Ferramenta, on_delete=models.DO_NOTHING)
    servidor = models.ForeignKey(Servidor, on_delete=models.DO_NOTHING)
    data = models.DateTimeField(auto_now_add=True, primary_key=True)

class Emprestimo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, related_name='emprestimos_feitos')
    reserva = models.ForeignKey(Reserva, on_delete=models.DO_NOTHING)
    dataRetirada = models.DateTimeField(auto_now_add=True)
    data_devolucao = models.DateTimeField(blank=True, null=True)
    responsavel_devolucao = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, blank=True, null=True)
    supervisor_devolucao = models.ForeignKey(Servidor, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='emprestimos_supervisionados')
