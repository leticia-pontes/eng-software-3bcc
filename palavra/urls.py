from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cadastro/", views.cadastro, name="cadastro"),
    path("jogo/", views.jogo, name="jogo"),
    path("configuracoes/", views.configuracoes, name="configuracoes"),
    path("ranking/", views.ranking, name="ranking"),
]