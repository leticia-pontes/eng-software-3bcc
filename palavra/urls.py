from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("entrar/", views.entrar, name="entrar"),
    path("cadastrar/", views.cadastrar, name="cadastrar"),
    path("jogo/", views.jogo, name="jogo"),
    path('pontos/', views.pontos_view, name='pontos_view'),
    path("configuracoes/", views.configuracoes, name="configuracoes"),
    path("ranking/", views.mostrar_ranking_melhores, name="ranking"),
    path("sair/", views.sair, name="sair"),
    path('deletar_conta/', views.deletar_conta, name='deletar_conta'),
]
