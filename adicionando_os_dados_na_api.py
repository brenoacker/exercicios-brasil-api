import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from exercicios.models import DDD, Regiao, SiglaEstado
from primeiro import dicionario_json1
from segundo import dicionario_json2
from terceiro import dicionario_json3, dicionario_json4, dicionario_json5

def pega_os_ddds():
    DDD.objects.all().delete()
    ddds_e_numero_cidades = dicionario_json1
    a = DDD(ddd = ddds_e_numero_cidades)
    a.save()

def pega_as_siglas():
    SiglaEstado.objects.all().delete()
    municipio_por_estado = dicionario_json2
    a = SiglaEstado(sigla = municipio_por_estado)
    a.save()

def pega_dados_terceiro_ex():
    Regiao.objects.all().delete()
    letra_a = dicionario_json3
    letra_b = dicionario_json4
    letra_c = dicionario_json5
    a = Regiao(A = letra_a, B = letra_b, C = letra_c)
    a.save()