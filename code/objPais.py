### OBJETO COUNTRY ###


class Country:
    ## FUNCAO QUE INICIALIZA UM OBJETO COUNTRY
    # Alterei todas as ocorrencias de "iso3116" por "iso3166" #Lauren
    # NAO FORAM TODAS AS OCORRENCIAS ACHEI UMA Q AINDA TAVA COMO 3116 HAA
    def __init__(self, name, capital, iso3166a2, iso3166a3, internetTLD,
                 callingCode, population, area, currencyName,
                 currency3letter, gdp, hdi, gini, lifeExp, continent,
                 coastArea, govForm, currInflation, tourism, currencyDolar):
        # area sera em km^2, GDP sera em milhoes de US$

        # Dados basicos
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

    ## GET-METHODS (em orientacao a objeto, eh boa praxe usar esses metodos para acessar os dados)

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
        # get-method para a variavel inicializada no metodo anterior
        return self.popDensity

    def compute_GDPperCapita(self):
        self.GDPperCapita = self.getGDP() / float(self.getPopulation())

    def get_GDPperCapita(self):
        # get-method para a variavel inicializada no metodo anterior
        return self.GDPperCapita

    # Adicionei esses dois metodos para criar o nome do arquivo de imagem #Lauren
    def set_map(self):
        return "../maps/" + self.iso3166a3 + ".gif"

    def set_flag(self):
        return "../flags/" + self.iso3166a3 + ".gif"

    # definir metodos para imprimir dados (para testes e quica para uma caixa de texto na versao final)
    # Para a caixa de texto, essa função não é necessária. Na versão final, proponho tirarmos esse método #Lauren

    # pois é, mas enquanto n tivermos com tudo pronto, ela é bem util
    # então, não tem problema deixar ela aqui, é só a gente n chamar ela #Henrique
    def showCountryData(self):
        self.compute_popDensity()
        self.compute_GDPperCapita()

        print("Country: ", self.getName())

        print('\nCurrency: ', self.getCurrencyName(), "(" + self.getCurrencyCode() + ")")
        print('\nISO-3116 alpha 2 Code: ', self.getIso3166a2())
        print("\nISO-3116 alpha 3 Code: ", self.getIso3166a3())
        print("\nInternet TLD: ", self.getInternetTLD())
        print("\nCalling code: ", self.getCallingCode())

        print("\n\nPopulation : ", self.getPopulation(), "inhabitants")
        print("\nCapital:", self.getCapital())
        print("\nArea: ", self.getArea(), "square kilometers")
        print("\nCoastal area: ", self.getCoast(), "kilometers")
        print("\nContinent: ", self.getContinent())
        print("\nPopulation density: ", self.get_popDensity(), "inhabitants per square kilometer")
        print("\nGovernment form: ", self.getGovernment())


        print("\n\nGDP: ", self.getGDP(), "USD")
        print("\nGDP per capita: ", self.get_GDPperCapita(), "USD per inhabitant")
        print("\nCurrent inflation rate: ", self.getInflation(), "percent on year")
        print("\nPercent of tourism on total exports: ", self.getTourism(), "percent")
        print("\nCurrent exchange ratio over the US dolar: ", self.getCurrencyDolar(), "as 1US$/currency (as dolars)")

        print("\n\nIDH: ", self.getIDH())
        print("\nGini index: ", self.getGINI())
        print("\nLife expectancy: ", self.getLifeExp(), 'years')


# coalition1.showCountryData()
# coalition2.showCountryData()
