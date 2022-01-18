from datetime import datetime, timedelta

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.http.response import Http404, JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from core import models

# Create your views here.


# def index(requests):
#     return redirect('/agenda/')

def login_user(request):
    return render(request, 'login.html')


def cadastro_user(request):
    return render(request, 'cadastro.html')


@require_POST
def cadastrar_user(request):
    usernome = request.POST['usernameC']
    email = request.POST['email']
    senha = request.POST['passwordC']

    teste1 = User.objects.get(username=usernome)
    teste2 = User.objects.get(email=email)

    if teste1 or teste2:
        messages.error(request, "Nome ou senha já existem, tente novamente!!!!!!")
    else:
        User.objects.create_user(username=usernome, email=email, password=senha)
        redirect('/')
    return redirect('/login/cadastro/')


def logout_user(requets):
    logout(requets)
    return redirect('/')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')  # método para recuperar os dados inseridos nas caixas de texto no
        # arquivo html, sendo o parâmetro buscado referenciado pelo nome username
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')  # esse if autentica se o usuário fez o login corretamente,
            # se sim, ele faz o login
            # e redireciona para a pagina padrão, no caso, o redirect('/') faz isso
        else:
            messages.error(request, "Usuário ou senha incorreta")
    return redirect('/')


@login_required(login_url='/login/')
def mostrarteste(request):
    return render(request, 'myclasses.html')


@login_required(login_url='/login/')
def executdef(request):
    dado = request.POST.get('insertdados')
    if dado:
        dados = models.LetraNumero(dado)
        retorno = {'defs': dados}
        return request, retorno
    else:
        messages.error(request, "Não foram passado dados")
        return redirect('/agenda')


@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user  # se eu quiser fazer um filtro por usuário conectado, devo colocar em vez de .all(),
    # .filter(usuario=usuario)
    data_atual = datetime.now() - timedelta(hours=1)  # o __gt significa que vc está pedindo as datas que são maiores
    # que a passada como parâmetro, se colocar __lt trás o que são menores
    evento = Evento.objects.filter(usuario=usuario, data_evento__gt=data_atual)  # esse .all() traz todos os
    # registros em uma lista
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)


@login_required(login_url='/login/')
def ver_historico(request):
    usuario = request.user
    data_atual = datetime.now()
    evento = Evento.objects.filter(usuario=usuario, data_evento__lt=data_atual)
    dados = {'eventos': evento}
    return render(request, 'historico.html', dados)


@login_required(login_url='/login/')
def dados_users(request):
    return render(request, 'dados.html')


@login_required(login_url='/login/')
def dados_alter(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = PasswordChangeForm(request.user, request.POST)
    if senha.is_valid():
        user = senha.save()
        update_session_auth_hash(request, user)
        User.objects.filter(user=request.user).update(username=nome, email=email)
    return redirect('/login/')


@login_required(login_url='/login/')
def evento(request):
    id_evento = request.GET.get('id')
    dado = {}
    if id_evento:
        dado['evento'] = Evento.objects.get(id=id_evento)
    return render(request, 'evento.html', dado)


@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descicao = request.POST.get('descricao')
        usuario = request.user
        id_evento = request.POST.get('id_evento')
        if id_evento:
            # evento = Evento.objects.get(id=id_evento)
            # if evento.usuario == usuario:
            #     evento.titulo = titulo
            #     evento.data_evento = data_evento
            #     evento.descicao = descicao
            #     evento.save(evento)
            Evento.objects.filter(id=id_evento).update(titulo=titulo, data_evento=data_evento, descicao=descicao)
        else:
            Evento.objects.create(titulo=titulo, data_evento=data_evento, descicao=descicao, usuario=usuario)
    return redirect('/')


@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    try:
        usuario = request.user
        evento = Evento.objects.get(id=id_evento)
        if usuario == evento.usuario:
            evento.delete()
        else:
            raise Http404()
        return redirect('/')
    except Exception:
        raise Http404


# @login_required(login_url='/login/')
# def deleta_conta(request, id_usuario):
#     try:
#         pedinte = request.user
#         cliente = User.objects.get(id=id_usuario)
#         if pedinte == cliente.usuario:
#             cliente.usuario.delete()
#         else:
#             raise Http404()
#         return redirect('/login/')
#     except Exception:
#         raise Http404


@login_required(login_url='/login/')
def json_lista_evento(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario).values('id', 'titulo')
    # se o parâmetro passado não for um dicionário, tem que usar o parâmetro safe=False
    return JsonResponse(list(evento), safe=False)
