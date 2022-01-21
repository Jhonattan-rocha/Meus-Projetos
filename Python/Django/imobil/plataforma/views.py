from tkinter import Image
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from random import randint
from plataforma.models import Imagens_nossas, Imovei, Cidade, Visitas


@login_required(login_url='/auth/logar/')
def home(request):
    cidades = Cidade.objects.all()
    preco_minimo = request.GET.get('preco_minimo')
    preco_maximo = request.GET.get('preco_maximo')
    cidade = request.GET.get('cidade')
    tipo = request.GET.getlist('tipo')
    if preco_minimo or preco_maximo or cidade or tipo:
        if not preco_minimo:
            preco_minimo = 0
        if not preco_maximo:
            preco_maximo = 999999999
        if not tipo:
            tipo = ['A', 'C']
        imoveis = Imovei.objects.filter(valor__gte=preco_minimo).filter(valor__lte=preco_maximo).filter(
            tipo_imovel__in=tipo).filter(cidade=cidade)
    else:
        imoveis = Imovei.objects.all()
    return render(request, 'home.html', {'imoveis': imoveis, 'cidades': cidades})


def imovel(request, id):
    imovel = get_object_or_404(Imovei, id=id)  # traz o objeto selecionado ou o erro 404
    sugestoes = Imovei.objects.filter(cidade=imovel.cidade).exclude(id=id)[:2]
    return render(request, 'imovel.html', {'imovel': imovel, 'sugestao': sugestoes, 'id': id})


def agendar_visitas(request):
    usuario = request.user
    dia = request.POST.get('dia')
    horario = request.POST.get('horario')
    id_imovel = request.POST.get('id_imovel')
    visita = Visitas(imovel_id=id_imovel, usuario=usuario, dia=dia, horario=horario)
    visita.save()
    return redirect('/agendamentos')


def agendamentos(request):
    visitas = Visitas.objects.filter(usuario=request.user)
    return render(request, "agendamentos.html", {'visitas': visitas})


def cancelar_agendamento(request, id):
    visitas = get_object_or_404(Visitas, id=id)
    visitas.status = "C"
    visitas.save()
    return redirect('/agendamentos')

def homepage(request):
    imoveis = Imovei.objects.filter(valor__gte=14100)
    imoveis_nossos = Imagens_nossas.objects.all()
    return render(request, 'homepage.html', {'imoveis': imoveis, 'imoveis_nossos': imoveis_nossos})


def apagar_imovel(request, id):
    imovel = Imovei.objects.filter(id=id)
    imovel.delete()
    print(request.user.get_group_permissions)
    return redirect('/')


def alterar(request, id):
    imovel = Imovei.objects.filter(id=id).values_list()
    return render(request, 'alterar.html', {'imovel_dados': imovel})
