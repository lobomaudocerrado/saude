from django.shortcuts import render
from registro.models import Pessoa, Meta, Peso
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

import datetime

def index(request):
    #return HttpResponse('Bem vindo')
    slug = request.POST.get('slug', None)
    try:
        pessoa = Pessoa.objects.get(slug=slug)
        return HttpResponseRedirect(reverse('peso',kwargs={'slug':pessoa.slug, }))
    except ObjectDoesNotExist:
        return HttpResponse(slug+' não está cadastrado.')



def peso(request, slug):
    """
    Constrói a página de registro do peso atual de uma pesoa.
    Utiliza como parâmetro o login -- será alterado para slug.
    login é usado para achar pessoa.
    pessoa é usada para buscar meta atual e histórico de pesos.
    pessoa, pesos e métrica atual são passadas em contexto.

    """

    ultimo = ""
    try:
        pessoa = Pessoa.objects.get(slug=slug)
    except ObjectDoesNotExist:
        return HttpResponse('Pessoa não cadstrada.')

    pesos = Peso.objects.filter(pessoa=pessoa)
    if pesos:
        ultimo = pesos[0]
    else:
        ultimo = ""

    meta = Meta.metaAtual(pessoa)
    contexto = {'pessoa':pessoa, 'meta':meta, 'pesos':pesos, 'ultimo':ultimo}


    return render(request, 'registra_peso.html', contexto)
"""
novoPeso(request)

insere o peso, id_pessoa enviados pelo metodo request.POST na classe Peso.
"""
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
        return HttpResponse('Problemas tentando salvar o peso, tente novamente mais tarde.')

    return HttpResponseRedirect(reverse('peso',kwargs={'slug':pessoa.slug, }))
