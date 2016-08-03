#Algoritmo para a geração dos nomes dos mapas/bandeiras

#se palavrasnonome > 1:
#	se 2ª = 'and': deixa só o 1ª
#	senão: concatena com 2ª
#se nomeatual = nomeanterior:
#	concatena com 3ª
#nomeanterior <= nomeatual

import os
import pycountry
import re

t = list(pycountry.countries)
nomeanterior = ''

for country in t:
    nome = country.name
    nomefinal = nome.lower()
    lista = re.split(' |, |-|\'', nome)
    if len(lista) > 1:
        if lista[1]== 'and' or lista[1][0] == '(':
            nomefinal = lista[0]
        else:
            nomefinal = lista[0] + lista[1]
        if nomefinal == nomeanterior:
            nomefinal = nomefinal + lista[2]
    nomeanterior = nomefinal
    alpha = country.alpha3
    old = os.path.abspath('../flags/' + nomefinal + '.gif')

    new = os.path.abspath('../flags/' + alpha + '.gif')

    if os.path.isfile(old):
        os.rename(old, new)
        print('Feito')

for country in t:
    nome = country.name
    nomefinal = nome.lower()
    lista = re.split(' |, |-|\'', nome)
    if len(lista) > 1:
        if lista[1]== 'and' or lista[1][0] == '(':
            nomefinal = lista[0]
        else:
            nomefinal = lista[0] + lista[1]
        if nomefinal == nomeanterior:
            nomefinal = nomefinal + lista[2]
    nomeanterior = nomefinal
    alpha = country.alpha3
    old = os.path.abspath('../maps/' + nomefinal + '.gif')

    new = os.path.abspath('../maps/' + alpha + '.gif')

    if os.path.isfile(old):
        os.rename(old, new)
        print('Feito')
