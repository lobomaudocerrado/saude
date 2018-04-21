from django.shortcuts import render
from registro.models import Pessoa, Meta, Peso
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

import datetime

def index(request):
    return HttpResponse('Bem vindo')


def peso(request, pessoa_login, mensagem=''):
    #pessoa = Pessoa()
    #pessoa.nome = pessoa_login + ': não cadastrado.'
    #meta = Meta()
    #meta.peso = 0
    #meta.data = datetime.datetime.now()
    #pesos = []
    pessoa_login = 'lobomaudocerrado@gmail.com'
    try:
        pessoa = Pessoa.objects.filter(login=pessoa_login)[0]
        #meta = Meta.objects.filter(pessoa = pessoa)

        pesos = Peso.objects.filter(pessoa=pessoa)
    except:
        pass
    meta = Meta.metaAtual(pessoa)
    contexto = {'pessoa':pessoa, 'meta':meta, 'pesos':pesos}

    if mensagem:
        contexto['mensagem'] = mensagem


    return render(request, 'registra_peso.html', contexto)

def novoPeso(request):

    try:
        pessoa = Pessoa.objects.get(id=request.POST.get('pessoa_id', None))
    except:
        return HttpResponse('Pessoa não encontrada.')

    try:
        peso = Peso()
        peso.pessoa = pessoa
        peso.peso = request.POST.get('peso')
        peso.save()
        mensagem = 'Peso registrado com sucesso.'
    except:
        mensagem = 'Erro ao registrar peso'

    return HttpResponseRedirect(reverse('peso',args=(pessoa.login, )), mensagem)
