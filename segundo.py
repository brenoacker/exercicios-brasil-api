#Pegar todas as 'siglas' de https://brasilapi.com.br/api/ibge/uf/v1
#Colocar em uma lista todas as UFs
#Fazer um loop que pegue todas as UFs em https://brasilapi.com.br/api/ibge/municipios/v1/{siglaUF}
#dentro do loop, contar o numero de municipios
#dentro do loop, fazer contagem de municipios

import requests, json

r = requests.get('https://brasilapi.com.br/api/ibge/uf/v1')
r_dict = r.json()

lista_siglas = []

i = 0
j = 0
k = 0

while i < len(r_dict):

    sigla_local = r_dict[i]['sigla']

    lista_siglas.append(sigla_local)
    
    i = i + 1

uf_numeromunicipios = {}
while j < len(lista_siglas):

    r_local = requests.get(f'https://brasilapi.com.br/api/ibge/municipios/v1/{lista_siglas[j]}')
    r_dict_local = r_local.json()
    
    sigla_local = lista_siglas[j]
    uf_numeromunicipios[sigla_local] = len(r_dict_local)

    j = j + 1


dicionario_json2 = {}

while k < len(lista_siglas):
    var = lista_siglas[k]

    if uf_numeromunicipios[var] == 1:
        dicionario_json2[lista_siglas[k]] = uf_numeromunicipios[var]

    else:
        dicionario_json2[lista_siglas[k]] = uf_numeromunicipios[var]

    k += 1


json_object = json.dumps(dicionario_json2, indent=4)

