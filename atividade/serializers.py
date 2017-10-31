from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from atividade.models import *
from django.conf.urls import url, include

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff')

class PessoaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pessoa
        fields = ('nome', 'email')

class EventoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Evento
        fields = ('nome',)

class TicketSerializer(serializers.HyperlinkedModelSerializer):
    evento = EventoSerializer(many=False)
    class Meta:
        model = Ticket
        fields = ('nome', 'descricao', 'valor', 'evento')

class InscricaoSerializer(serializers.HyperlinkedModelSerializer):
    pessoa = PessoaSerializer(many=False)
    ticket = TicketSerializer(many=False)
    evento = EventoSerializer(many=False)
    class Meta:
        model = Inscricao
        fields = ('pessoa', 'ticket', 'evento', 'validacao')
