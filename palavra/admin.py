from django.contrib import admin

from .models import Usuario, Tema, Palavra

admin.site.register(Usuario)
admin.site.register(Tema)
admin.site.register(Palavra)