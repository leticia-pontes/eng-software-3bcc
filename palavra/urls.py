from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("entrar/", views.entrar, name="entrar"),
    path("cadastrar/", views.cadastrar, name="cadastrar"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("jogo/", views.jogo, name="jogo"),
    path('get_pontuacao/', views.get_pontuacao, name='get_pontuacao'),
    path("configuracoes/", views.configuracoes, name="configuracoes"),
    path("ranking/", views.mostrar_ranking_melhores, name="mostrar_ranking_melhores"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
