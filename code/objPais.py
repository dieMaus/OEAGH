### OBJETO COUNTRY ###


class Country:

	## FUNCAO QUE INICIALIZA UM OBJETO COUNTRY
	#Alterei todas as ocorrencias de "iso3116" por "iso3166" #Lauren
	def __init__(self, name, capital, largestCity, iso3166, internetTLD, callingCode, population, area, currencyName, currency3letter, gdp, hdi, gini):
		# area sera em km^2, GDP sera em US$
	
		# Dados basicos
		self.name = name
		self.capital = capital
		self.largestCity = largestCity
		
		#(flag and map?)
		
		# Siglas
		self.iso3166 = iso3166
		self.internetTLD = internetTLD
		self.callingCode = callingCode
		
		# Dados geograficos
		self.population = population
		self.area = area
		self.currencyName = currencyName
		self.currency3letter = currency3letter
		
		# Indicadores sociopoliticos
		self.gdp = gdp
		self.hdi = hdi
		self.gini = gini
	
	## GET-METHODS (em orientacao a objeto, eh boa praxe usar esses metodos para acessar os dados)
	
	def get_name(self):
		return self.name
		
	def get_capital(self):
		return self.capital
		
	def get_largestCity(self):
		return self.largestCity
		
	def get_iso3166(self):
		return self.iso3166
		
	def get_internetTLD(self):
		return self.internetTLD
		
	def get_callingCode(self):
		return self.callingCode
		
	def get_population(self):
		return self.population
		
	def get_area(self):
		return self.area
		
	def get_currencyName(self):
		return self.currencyName
	
	def get_currency3letter(self):
		return self.currency3letter
		
	def get_gdp(self):
		return self.gdp
		
	def get_hdi(self):
		return self.hdi
		
	def get_gini(self):
		return self.gini
		
	
	# definir os metodos de dados compostos (PIB per capita, etc)
	
	def capital_is_largest_city(self):
		# Checa se a capital do pais eh tambem a maior cidade, usando comparacao de string
		if self.get_capital() == self.get_largestCity():
			return True
		else:
			return False
			
	def compute_popDensity(self):
		self.popDensity = float(self.get_population()) / self.get_area()
		
	def get_popDensity(self):
		# get-method para a variavel inicializada no metodo anterior
		return self.popDensity
		
	def compute_GDPperCapita(self):
		self.GDPperCapita = self.get_gdp() / float(self.get_population())
		
	def get_GDPperCapita(self):
		# get-method para a variavel inicializada no metodo anterior
		return self.GDPperCapita
	
	#Adicionei esses dois metodos para criar o nome do arquivo de imagem #Lauren
	def set_map(self):
		return "Maps/" + self.iso3166 + ".gif"
	
	def set_flag(self):
		return "Flags/" + self.iso3166 + ".gif"
		
	# definir metodos para imprimir dados (para testes e quica para uma caixa de texto na versao final)
	#Para a caixa de texto, essa função não é necessária. Na versão final, proponho tirarmos esse método #Lauren
	def showCountryData(self):
		self.compute_popDensity()
		self.compute_GDPperCapita()
		
		print "Country:", self.get_name()
		
		if self.capital_is_largest_city():
			print "Its capital is", self.get_capital() + ", which is also its largest city."	
		else:
			print "Its capital is", self.get_capital() + ", and its largest city is", self.get_largestCity() + "."
		
		print "\nCurrency:", self.get_currencyName(), "(" + self.get_currency3letter() + ")"
		print "ISO-3116 Code:", self.get_iso3116()
		print "Internet TLD:", self.get_internetTLD()
		print "Calling Code:", self.get_callingCode()
		
		print "\nPopulation:", self.get_population(), "inhabitants"
		print "Area:", self.get_area(), "square kilometers"
		print "Population Density:", self.get_popDensity(), "inhabitants per square kilometer"
		
		print "\nGDP:", self.get_gdp(), "USD"
		print "GDP per capita:", self.get_GDPperCapita(), "USD per inhabitant"
		
		print "\nHDI:", self.get_hdi()
		
		print "\nGini index:", self.get_gini()

## TESTEZINHO BASICO

# teste com dados inventados e capital nao sendo maior cidade
coalition1 = Country("Western Coalition", "Facao", "Fhreired", "WC", ".wc", "+23", 800000, 45000, "Kopeki", "KOP", 56000000, 0.937, 0.600)

# teste com dados inventados e capital sendo maior cidade
coalition2 = Country("Western Coalition", "Fhreired", "Fhreired", "WC", ".wc", "+23", 800000, 45000, "Kopeki", "KOP", 56000000, 0.937, 0.600)

# coalition1.showCountryData()
# coalition2.showCountryData()
