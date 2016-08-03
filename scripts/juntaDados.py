import os
import csv

fieldnames = ['name', 'capital', 'largestCity',
              'iso3166-a3', 'iso3166-a2', 'internetTLD', 'callingCode',
              'population', 'area', 'currencyName',
              'currency3letter', 'gdp', 'idh', 'gini',
              'lifeExp', 'continent', 'coastArea',
              'govForm', 'currentInflation', 'tourism', 'currency/dolar']


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
                           'n.a.', 'n.a.', 'n.a.', 'n.a.', 'n.a.', 'n.a.', 'n.a.'])

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
                linhaPai[16] = linha['Coastline']
                linhaPai[17] = linha['Government form'].capitalize()
                linhaPai[14] = linha['Life expectancy']
                break
        else:
            # país não esta na lista do arquivo principal
            continue

with open(os.path.abspath('../country_data/currencies.csv'), newline='', encoding='utf-8') as money:
    reader = csv.DictReader(money)
    for linha in reader:
        for linhaPai in master:
            if linha['Codigo'] == linhaPai[10]:
                linhaPai[20] = linha['Unidades1USD']
                break
        else:
            # moeda não esta na lista do arquivo principal
            continue
    for linhaPai in master:
        if linhaPai[10] == 'USD':
            linhaPai[20] = '1'
            continue
        if linhaPai[10] == 'EUR':
            linhaPai[20] = '0.8884'
            continue
        if linhaPai[10] == 'XAF':
            linhaPai[20] = '582.657'
            continue
        if linhaPai[10] == 'XCD':
            linhaPai[20] = '2.7169'
            continue
        if linhaPai[10] == 'XOF':
            linhaPai[20] = '591.096'
            continue
        if linhaPai[10] == 'ZAR':
            linhaPai[20] = '15.2509'
            continue
        if linhaPai[10] == 'INR':
            linhaPai[20] = '67.2775'
            continue

with open(os.path.abspath('../country_data/surface area.csv'), newline='') as area:
    reader = csv.DictReader(area)
    for linha in reader:
        for linhaPai in master:
            if linha['Country Code'] == linhaPai[3]:
                ano = 2015
                while not linha[str(ano)]:
                    ano -= 1
                    if ano == 1960:
                        break
                else:
                    linhaPai[8] = linha[str(ano)]
                break
        else:
            # país não esta na lista do arquivo principal
            continue

with open(os.path.abspath('../country_data/GDP 2015.csv'), newline='') as gdp:
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

with open(os.path.abspath('../country_data/GINI 2015.csv'), newline='') as gini:
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

with open(os.path.abspath('../country_data/population 2015.csv'), newline='') as pop:
    reader = csv.DictReader(pop)
    for linha in reader:
        for linhaPai in master:
            if linha['Country Code'] == linhaPai[3]:
                ano = 2015
                while not linha[str(ano)]:
                    ano -= 1
                    if ano == 1960:
                        break
                else:
                    linhaPai[7] = linha[str(ano)]
                break
        else:
            # país não esta na lista do arquivo principal
            continue

with open(os.path.abspath('../country_data/tourism on percent of exports.csv'), newline='') as pop:
    reader = csv.DictReader(pop)
    for linha in reader:
        for linhaPai in master:
            if linha['Country Code'] == linhaPai[3]:
                ano = 2015
                while not linha[str(ano)]:
                    ano -= 1
                    if ano == 1960:
                        break
                else:
                    linhaPai[19] = linha[str(ano)]
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

with open(os.path.abspath('../country_data/inflacao 2015.csv'), newline='') as inflacao:
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
