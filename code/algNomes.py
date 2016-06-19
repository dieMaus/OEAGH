#Algoritmo para a geração dos nomes dos mapas/bandeiras

#se palavrasnonome > 1:
#	se 2ª = 'and': deixa só o 1ª
#	senão: concatena com 2ª
#se nomeatual = nomeanterior:
#	concatena com 3ª
#nomeanterior <= nomeatual

#Soh nao substitui os nomes que eu digitei errado ou que tem acento :/
#Eu digitei muitos nomes errados
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
    old = "C:/Users/Laure/OneDrive/Documentos/CPD/TrabalhoFinal/Flags" + "/" + nomefinal + ".gif"
    #^^^^^Substitua pelo seu path ^^^^^^
    new = "C:/Users/Laure/OneDrive/Documentos/CPD/TrabalhoFinal/Flags" + "/" + alpha + ".gif"
    #^^^^^Substitua pelo seu path ^^^^^^

    if os.path.isfile(old):
        os.rename(old, new)
        print('Feito')
