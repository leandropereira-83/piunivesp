from django.contrib import admin
from .models import UC, Atividade, Comentario, NotaAula

admin.site.register(UC)
admin.site.register(Atividade)
admin.site.register(Comentario)
admin.site.register(NotaAula)