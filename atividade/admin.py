from django.contrib import admin

from .models import Pessoa, Evento, Ticket, Inscricao
admin.site.register(Pessoa)
admin.site.register(Evento)
admin.site.register(Ticket)
admin.site.register(Inscricao)
