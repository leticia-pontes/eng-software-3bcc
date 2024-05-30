from django.contrib import admin

from .models import Cadastro, Tema, Palavra

admin.site.register(Cadastro)
admin.site.register(Tema)
admin.site.register(Palavra)