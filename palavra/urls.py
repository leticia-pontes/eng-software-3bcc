from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("popup/", views.popup, name="popup"),
    path("jogo/", views.jogo, name="jogo"),
    path("configuracoes/", views.configuracoes, name="configuracoes"),
]