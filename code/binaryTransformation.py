import csv
import os
import pickle
import objPais

database = open(os.path.abspath('../country_data/fullData.csv'), newline='')
endpoint = open(os.path.abspath('../data/binaries.kbb'), 'wb')
reader = csv.DictReader(database)

for pais in reader:
    buffer = objPais.Country(pais['name'], pais['capital'], pais['iso3166-a2'], pais['iso3166-a3'],
                            pais['internetTLD'], pais['callingCode'], pais['population'],
                            pais['area'], pais['currencyName'], pais['currency3letter'],
                            pais['gdp'], pais['idh'], pais['gini'], pais['lifeExp'],
                            pais['continent'], pais['coastArea'], pais['govForm'],
                            pais['currentInflation'], pais['tourism'], pais['currency/dolar'])
    pickle.dump(buffer, endpoint)

database.close()