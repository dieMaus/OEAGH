# olar
# eu tentei ser o mais correto possivel
# mas vai que eu esteja errado né, então sinta-se a vontade pra arrumar

# usei o with open... as ... pq vi varios exemplos na internet desse jeito

import os
import csv

fieldnames = ['name', 'capital', 'largestCity', 'iso3116', 'internetTLD', 'callingCode',
              'population', 'area', 'currencyName', 'currency3letter', 'gdp', 'hdi', 'gini']

final = open(os.path.abspath('../country_data/fullData.csv'), 'w')

writer = csv.DictWriter(final, fieldnames=fieldnames)
writer.writeheader()

with open(os.path.abspath('../country_data/country-codes.csv'), newline='') as codes:
    reader = csv.DictReader(codes)
    for linha in reader:
        if linha['is_independent'] is 'yes':
            writer.writerow({'name': linha['official_name'],
                             'iso3116': linha['ISO3166-1-Alpha-3'],
                             'callingCode': linha['Dial'],
                             'currency3letter': linha['currency_alphabetic_code'],
                             'currencyName': linha['currency_name']})
    readerPai = csv.DictReader(final)

with open(os.path.abspath('../country_data/country-list.csv'), newline='') as capitals:
    reader = csv.DictReader(capitals)
    for linha in reader:
        for linhaPai in readerPai:
            if linha['country'] == linhaPai['name']:
                break
        else:
            # país não esta na lista do arquivo principal
            continue
        writer.writerow({'capital': linha['capital']})

with open(os.path.abspath('../country_data/GDP spam 1960-2015.csv'), newline='') as gdp:
    reader = csv.DictReader(gdp)
    for linha in reader:
        for linhaPai in readerPai:
            if linha['Country Name'] == linhaPai['name']:
                break
        else:
            # país não esta na lista do arquivo principal
            continue

        ano = 2015
        while not linha[str(ano)]:
            ano -= 1
            if ano == 1960:
                break
        else:
            writer.writerow({'gdp': linha[str(ano)]})

with open(os.path.abspath('../country_data/GINI spam 1960-2015.csv'), newline='') as gini:
    reader = csv.DictReader(gini)
    for linha in reader:
        for linhaPai in readerPai:
            if linha['Country Name'] == linhaPai['name']:
                break
        else:
            # país não esta na lista do arquivo principal
            continue

        ano = 2015
        while not linha[str(ano)]:
            ano -= 1
            if ano == 1960:
                break
        else:
            writer.writerow({'gini': linha[str(ano)]})

with open(os.path.abspath('../country_data/POP spam 1980-2010.csv'), newline='') as pop:
    reader = csv.DictReader(pop)
    for linha in reader:
        for linhaPai in readerPai:
            if linha['Country Name'] == linhaPai['name']:
                break
        else:
            # país não esta na lista do arquivo principal
            continue

        ano = 2015
        while not linha[str(ano)]:
            ano -= 1
            if ano == 1960:
                break
        else:
            writer.writerow({'population': linha[str(ano)]})

with open(os.path.abspath('../country_data/surfaceArea spam 1960-2015.csv'), newline='') as area:
    reader = csv.DictReader(area)
    for linha in reader:
        for linhaPai in readerPai:
            if linha['Country Name'] == linhaPai['name']:
                break
        else:
            # país não esta na lista do arquivo principal
            continue

        ano = 2015
        while not linha[str(ano)]:
            ano -= 1
            if ano == 1960:
                break
        else:
            writer.writerow({'area': linha[str(ano)]})

with open(os.path.abspath('../country_data/IDH 2014.csv'), newline='') as idh:
    reader = csv.DictReader(idh)
    for linha in reader:
        for linhaPai in readerPai:
            if linha['country'] == linhaPai['Country Name']:
                break
        else:
            # país não esta na lista do arquivo principal
            continue

        writer.writerow({'hdi': linha['2014']})