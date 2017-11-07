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
    def create(self, validated_data):
        return Pessoa.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.nome = validated_data.get('nome', instance.nome)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance

class EventoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Evento
        fields = ('nome',)
    def create(self, validated_data):
        return Evento.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome', instance.nome)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance

class TicketSerializer(serializers.HyperlinkedModelSerializer):
    evento = EventoSerializer(many=True)
    class Meta:
        model = Ticket
        fields = ('nome', 'descricao', 'valor', 'evento')
    def created(self, validated_data):
        eventos = validated_data.pop('evento')
        Ticket.objects.create(**validated_data)
        for evento in eventos:
            evento.objects.create(eventoformat = eventoformat, **evento_data)
        return eventoformat

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome', instance.nome)
        instance.descricao = validated_data.get('descricao', instance.descricao)
        instance.valor = validated_data.get('valor', instance.valor)
        instance.Evento = validated_data.get('Evento', instance.Evento)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance

class InscricaoSerializer(serializers.HyperlinkedModelSerializer):
    pessoa = PessoaSerializer(many=False)
    ticket = TicketSerializer(many=False)
    evento = EventoSerializer(many=False)
    class Meta:
        model = Inscricao
        fields = ('pessoa', 'ticket', 'evento', 'validacao')
