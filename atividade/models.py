from django.db import models

class Pessoa(models.Model):
    nome = models.CharField('nome', max_length=200)
    email = models.EmailField('email')

    def __str__(self):
        return self.nome

class Evento(models.Model):
    nome = models.TextField('nome')

    def __str__(self):
        return self.nome

class Ticket(models.Model):
    nome = models.TextField('nome')
    descricao = models.TextField('descricao')
    valor = models.FloatField('valor')
    Evento = models.ForeignKey('Evento')

    def __str__(self):
        return self.nome

class Inscricao(models.Model):
    Pessoa = models.ForeignKey('Pessoa')
    Ticket = models.ForeignKey('Ticket')
    Evento = models.ForeignKey('Evento')
    validacao = models.BooleanField('validacao')
