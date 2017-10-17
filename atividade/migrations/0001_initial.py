# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-17 00:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField(verbose_name='nome')),
            ],
        ),
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('validacao', models.BooleanField(verbose_name='validacao')),
                ('Evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atividade.Evento')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='nome')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField(verbose_name='nome')),
                ('descricao', models.TextField(verbose_name='descricao')),
                ('valor', models.FloatField(verbose_name='valor')),
                ('Evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atividade.Evento')),
            ],
        ),
        migrations.AddField(
            model_name='inscricao',
            name='Pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atividade.Pessoa'),
        ),
        migrations.AddField(
            model_name='inscricao',
            name='Ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atividade.Ticket'),
        ),
    ]
