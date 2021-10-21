from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets, generics
from exercicios.models import Regiao, DDD, SiglaEstado
from exercicios.serializer import RegiaoSerializer, DDDSerializer, SiglaEstadoSerializer
from adicionando_os_dados_na_api import pega_dados_terceiro_ex, pega_os_ddds, pega_as_siglas

class Exercicio1ViewSet(viewsets.ModelViewSet):
    """Exibe os top 5 ddds que ocorrem no maior número de cidades do Brasil e o número de cidades"""
    pega_os_ddds()
    queryset = DDD.objects.all()
    serializer_class = DDDSerializer
    http_method_names = ['get',]

class Exercicio2ViewSet(viewsets.ModelViewSet):
    """Lista o número de municípios de cada estado do Brasil"""
    pega_as_siglas()
    queryset = SiglaEstado.objects.all()
    serializer_class = SiglaEstadoSerializer
    http_method_names = ['get',]

class Exercicio3ViewSet(viewsets.ModelViewSet):
    """ \n A) Lista quantos CNPJs estão localizados em cada região do Brasil \n B) Lista a média de sócios das empresas por região \n C) Lista o número de empresas que tem mais de 2 cnaes secundárias cadastradas."""
    pega_dados_terceiro_ex()
    queryset = Regiao.objects.all()
    serializer_class = RegiaoSerializer
    http_method_names = ['get',]