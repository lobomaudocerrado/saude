from django.shortcuts import render
from registro.models import Pessoa, Meta, Peso
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

import datetime

def index(request):
    return HttpResponse('Bem vindo')


def peso(request, pessoa_login):
    #pessoa = Pessoa()
    #pessoa.nome = pessoa_login + ': não cadastrado.'
    #meta = Meta()
    #meta.peso = 0
    #meta.data = datetime.datetime.now()
    #pesos = []
    pessoa_login = 'lobomaudocerrado@gmail.com'
    try:
        pessoa = Pessoa.objects.filter(login=pessoa_login)[0]
        meta = Meta.objects.filter(pessoa = pessoa)[0]
        pesos = Peso.objects.filter(pessoa=pessoa)
    except:
        pass

    contexto = {'pessoa':pessoa, 'meta':meta, 'pesos':pesos}


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
    except:
        return HttpResponse('Erro ao salvar o peso')

    return HttpResponseRedirect(reverse('peso',args=(pessoa.login,)))
