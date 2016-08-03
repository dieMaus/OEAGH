### OBJETO COUNTRY ###


class Country:
    ## FUNÇÃO QUE INICIALIZA UM OBJETO COUNTRY
    def __init__(self, name, capital, iso3166a2, iso3166a3, internetTLD,
                 callingCode, population, area, currencyName,
                 currency3letter, gdp, hdi, gini, lifeExp, continent,
                 coastArea, govForm, currInflation, tourism, currencyDolar):
        # area é em km², GDP é em US$

        # Dados básicos
        self.name = name
        self.capital = capital

        # Siglas
        self.iso3166a2 = iso3166a2
        self.iso3166a3 = iso3166a3
        self.internetTLD = internetTLD
        self.callingCode = callingCode

        # Dados geograficos
        self.population = population
        self.area = area
        self.continent = continent
        self.coastArea = coastArea

        # Indicadores sociopoliticos
        self.hdi = hdi
        self.gini = gini
        self.lifeExp = lifeExp
        self.government = govForm

        # Indicadores economicos
        self.gdp = gdp
        self.currency3letter = currency3letter
        self.currencyName = currencyName
        self.inflation = currInflation
        self.tourism = tourism
        self.currencyExchange = currencyDolar

    ## GET-METHODS (em orientacao a objeto, é boa praxe usar esses métodos para acessar os dados)

    def getName(self):
        return self.name

    def getCapital(self):
        return self.capital

    def getIso3166a2(self):
        return self.iso3166a2

    def getIso3166a3(self):
        return self.iso3166a3

    def getInternetTLD(self):
        return self.internetTLD

    def getCallingCode(self):
        return self.callingCode

    def getPopulation(self):
        return self.population

    def getArea(self):
        return self.area

    def getCurrencyName(self):
        return self.currencyName

    def getCurrencyCode(self):
        return self.currency3letter

    def getGDP(self):
        return self.gdp

    def getIDH(self):
        return self.hdi

    def getGINI(self):
        return self.gini

    def getLifeExp(self):
        return self.lifeExp

    def getContinent(self):
        return self.continent

    def getCoast(self):
        return self.coastArea

    def getGovernment(self):
        return self.government

    def getInflation(self):
        return self.inflation

    def getTourism(self):
        return self.tourism

    def getCurrencyDolar(self):
        return self.currencyExchange

    # definir os metodos de dados compostos (PIB per capita, etc)

    def compute_popDensity(self):
        self.popDensity = float(self.getPopulation()) / self.getArea()

    def get_popDensity(self):
        return self.popDensity

    def compute_GDPperCapita(self):
        self.GDPperCapita = self.getGDP() / float(self.getPopulation())

    def get_GDPperCapita(self):
        return self.GDPperCapita

    # Criar o nome do arquivo de imagem
    def return_path_map(self):
        import os
        return os.path.abspath('../maps/' + self.iso3166a3 + '.gif')

    def return_path_flag(self):
        import os
        return os.path.abspath('../flags/' + self.iso3166a3 + '.gif')

   
