"""projeto_curso_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/', views.lista_eventos),
    path('agenda/lista', views.json_lista_evento),
    path('', RedirectView.as_view(url='/agenda/')),
    # path('', views.index)
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('login/cadastro/', views.cadastro_user),
    path('login/cadastro/submit', views.cadastrar_user),
    path('logout/', views.logout_user),
    path('agenda/evento/', views.evento),
    path('agenda/evento/submit', views.submit_evento),
    path('agenda/evento/delete/<int:id_evento>/', views.delete_evento),
    path('historico/', views.ver_historico),
    path('historico/delete/<int:id_evento>/', views.delete_evento),
    path('agenda/dados/', views.dados_users),
    path('agenda/dados/submit', views.dados_alter),
    path('agenda/teste/', views.mostrarteste),
    path('agenda/teste/submit', views.executdef)
]

