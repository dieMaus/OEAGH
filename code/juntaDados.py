# olar
# eu tentei ser o mais correto possivel
# mas vai que eu esteja errado né, então sinta-se a vontade pra arrumar

# usei o with open... as ... pq vi varios exemplos na internet desse jeito

import os
import csv

fieldnames = ['name', 'capital', 'largestCity',
              'iso3166-a3', 'iso3166-a2', 'internetTLD', 'callingCode',
              'population', 'area', 'currencyName',
              'currency3letter', 'gdp', 'idh', 'gini',
              'lifeExp', 'continent', 'coastArea',
              'govForm', 'currentInflation']

# na minha matriz vai ficar assim
# ['name', 'capital', 'largestCity','iso3166-a3', 'iso3166-a2', 'internetTLD', 'callingCode','population', 'area', 'currencyName','currency3letter', 'gdp', 'idh', 'gini']
# ['paraguay','assuncion','etc',...
#
# vou alterando os dados incompletos da matriz enquanto leio todos os arquivos csv que eu tenho
# e no final escrevo essa matriz mestre no arquivo csv final


final = open(os.path.abspath('../country_data/fullData.csv'), 'w+', newline='')

writer = csv.writer(final, quoting=csv.QUOTE_ALL)

master = []
master.append(fieldnames)

with open(os.path.abspath('../country_data/country-codes.csv'), newline='') as codes:
    reader = csv.DictReader(codes)
    for linha in reader:
        if linha['is_independent'] == 'Yes':
            master.append([linha['official_name'], 'n.a.', 'n.a.',
                           linha['ISO3166-1-Alpha-3'], linha['ISO3166-1-Alpha-2'], 'n.a.', linha['Dial'],
                           'n.a.', 'n.a.', linha['currency_name'],
                           linha['currency_alphabetic_code'], 'n.a.', 'n.a.', 'n.a.',
                           'n.a.', 'n.a.', 'n.a.', 'n.a.', 'n.a.'])

with open(os.path.abspath('../country_data/capitals.csv'), newline='', encoding='utf-8') as capitals:
    reader = csv.DictReader(capitals)
    for linha in reader:
        for linhaPai in master:
            if linha['Country code'] == linhaPai[4]:
                linhaPai[1] = linha['City (en)']
                break
        else:
            # país não esta na lista do arquivo principal
            continue

with open(os.path.abspath('../country_data/countries.csv'), newline='', encoding='utf-8') as general:
    reader = csv.DictReader(general)
    for linha in reader:
        for linhaPai in master:
            if linha['Country code'] == linhaPai[4]:
                linhaPai[15] = linha['Continent']
                linhaPai[7] = linha['Population']
                linhaPai[8] = linha['Area']
                linhaPai[16] = linha['Coastline']
                linhaPai[17] = linha['Government form'].capitalize()
                linhaPai[14] = linha['Life expectancy']
                break
        else:
            # país não esta na lista do arquivo principal
            continue

with open(os.path.abspath('../country_data/GDP spam 1960-2015.csv'), newline='') as gdp:
    reader = csv.DictReader(gdp)
    for linha in reader:
        for linhaPai in master:
            if linha['Country Code'] == linhaPai[3]:
                ano = 2015
                while not linha[str(ano)]:
                    ano -= 1
                    if ano == 1960:
                        break
                else:
                    linhaPai[11] = linha[str(ano)]
                break
        else:
            # país não esta na lista do arquivo principal
            continue

with open(os.path.abspath('../country_data/GINI spam 1960-2015.csv'), newline='') as gini:
    reader = csv.DictReader(gini)
    for linha in reader:
        for linhaPai in master:
            if linha['Country Code'] == linhaPai[3]:
                ano = 2015
                while not linha[str(ano)]:
                    ano -= 1
                    if ano == 1960:
                        break
                else:
                    linhaPai[13] = linha[str(ano)]
                break
        else:
            # país não esta na lista do arquivo principal
            continue

with open(os.path.abspath('../country_data/IDH 2014.csv'), newline='') as idh:
    reader = csv.DictReader(idh)
    for linha in reader:
        for linhaPai in master:
            if linha['Country'] == linhaPai[0]:
                linhaPai[12] = linha['2014']
                break
        else:
            # país não esta na lista do arquivo principal
            continue

with open(os.path.abspath('../country_data/Inflacao data spam 1980-2015.csv'), newline='') as inflacao:
    reader = csv.DictReader(inflacao)
    for linha in reader:
        for linhaPai in master:
            if linha['Country Code'] == linhaPai[3]:
                ano = 2015
                while not linha[str(ano)]:
                    ano -= 1
                    if ano == 1960:
                        break
                else:
                    linhaPai[18] = linha[str(ano)]
                break
        else:
            # país não esta na lista do arquivo principal
            continue

with open(os.path.abspath('../country_data/basicamente tld.csv'), newline='') as tld:
    reader = csv.DictReader(tld)
    for linha in reader:
        for linhaPai in master:
            if linha['ISO 3166-1 3 Letter Code'] == linhaPai[3]:
                linhaPai[5] = linha['IANA Country Code TLD']
                break
        else:
            # país não esta na lista do arquivo principal
            continue

writer.writerows(master)

final.close()
