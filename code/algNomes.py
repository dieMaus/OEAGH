# Algoritmo para a geração dos nomes dos mapas/bandeiras

# se palavrasnonome > 1:
#	se 2ª = 'and': deixa só o 1ª
#	senão: concatena com 2ª
# se nomeatual = nomeanterior:
#	concatena com 3ª
# nomeanterior <= nomeatual

# Soh nao substitui os nomes que eu digitei errado ou que tem acento :/
# Eu digitei muitos nomes errados
import os
import pycountry
import csv
import re

database = open(os.path.abspath('../country_data/fullData.csv'), newline='')
reader = csv.DictReader(database)

t = list(pycountry.countries)
nomeanterior = ''

for country in reader:
    nome = country.name
    nomefinal = nome.lower()
    lista = re.split(' |, |-|\'', nome)
    if len(lista) > 1:
        if lista[1] == 'and' or lista[1][0] == '(':
            nomefinal = lista[0]
        else:
            nomefinal = lista[0] + lista[1]
        if nomefinal == nomeanterior:
            nomefinal = nomefinal + lista[2]
    nomeanterior = nomefinal
    alpha = country['iso3166-a3']

    old = os.path.abspath('../flags/' + nomefinal + '.gif')

    new = os.path.abspath('../flags/' + alpha + '.gif')

    if os.path.isfile(old):
        os.rename(old, new)
        print('Feito!')

for country in reader:
    nome = country.name
    nomefinal = nome.lower()
    lista = re.split(' |, |-|\'', nome)
    if len(lista) > 1:
        if lista[1] == 'and' or lista[1][0] == '(':
            nomefinal = lista[0]
        else:
            nomefinal = lista[0] + lista[1]
        if nomefinal == nomeanterior:
            nomefinal = nomefinal + lista[2]
    nomeanterior = nomefinal
    alpha = country['iso3166-a3']

    old = os.path.abspath('../maps/' + nomefinal + '.gif')

    new = os.path.abspath('../maps/' + alpha + '.gif')

    if os.path.isfile(old):
        os.rename(old, new)
        print('Feito!')
