#improved GUI

import tkinter as tk
from tkinter import END, LEFT, RIGHT, CURRENT
from PIL import Image
from unidecode import unidecode
import pycountry
import objPais
import btree
import pickle
import os

LARGE_FONT = ("Verdana", 12)

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, SelExibe, SelLista, SelCompara):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)
        
    #Exibe um novo frame
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
    
    #Fecha o aplicativo
    def quit_it(self):
        self.destroy()

    #Exibe uma nova janela, exibindo os dados do pais anteriormente selecionado
    def Display(self, country):
        frame = tk.Toplevel(self)
        
        #Exibe o nome do pais, assim como o usuário o digitou
        label = tk.Label(frame, text="%s" %(country))
        label.grid(row=0, column=2)
        
        #Seta scrollbar e text box
        S = tk.Scrollbar(frame)
        T = tk.Text(frame, height=10, width=50)
        S.grid(pady=2, padx=2, row=2, column=0)
        T.grid(pady=2, padx=2, row=2, column=1, columnspan=3)
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)

        #Para pastas irmas, usar o '../' antes de Btrees
        bname = open("../data/Btrees/names.pkl", 'rb')

        #Inicializa e desserializa a arvore B
        b = btree.BTree(4)
        b = pickle.load(bname)
        nodo = b.show([country])
        index = nodo[1] #Recebe o indice (usado como ponteiro) para o arquivo binario

        bname.close()

        binary = open("../data/Btrees/binaries.kbb", 'rb')
        for num in range(0, index):     
            count = pickle.load(binary) #Recebe o pais de indice 'index'

        binary.close()

        #Seta path para mapa e bandeira
        mapa = count.return_path_map() 
        flag = count.return_path_flag()

        #Bandeira do pais
        #Cria imagem temporaria reduzida
        im_temp = Image.open(flag)
        im_temp = im_temp.resize((175, 90), Image.ANTIALIAS)
        im_temp.save("teste.gif", "gif")
        
        flag = tk.PhotoImage(file="teste.gif")
        painel11 = tk.Label(frame, image = flag)
        painel11.image = flag
        painel11.grid(row=1, column=1)

        #Mapa do pais
        im_temp = Image.open(mapa)
        im_temp = im_temp.resize((175, 90), Image.ANTIALIAS)
        im_temp.save("teste.gif", "gif")
        
        mapa = tk.PhotoImage(file="teste.gif")
        painel1 = tk.Label(frame, image = mapa)
        painel1.image = mapa
        painel1.grid(row=1, column=3)
        
        #Exibicao do objeto Pais selecionado (modo naive)
        T.insert(CURRENT, "Capital:\t\t" + count.capital + '\n')
        T.insert(CURRENT, "ISO3166a2:\t\t" + count.iso3166a2 + '\n')
        T.insert(CURRENT, "ISO3166a3:\t\t" + count.iso3166a3 + '\n')
        T.insert(CURRENT, "Internet TLD:\t\t" + count.internetTLD + '\n')
        T.insert(CURRENT, "Calling Code:\t\t" + count.callingCode + '\n')
        T.insert(CURRENT, "Continent:\t\t" + count.continent + '\n')
        T.insert(CURRENT, "Government:\t\t" + count.government + '\n')
        T.insert(CURRENT, "Population:\t\t" + str(count.population) + '\n')
        T.insert(CURRENT, "Area:\t\t" + str(count.area) + '\n')
        T.insert(CURRENT, "Coast Area:\t\t" + str(count.coastArea) + '\n')
        T.insert(CURRENT, "HDI:\t\t" + str(count.hdi) + '\n')
        T.insert(CURRENT, "GINI:\t\t" + str(count.gini) + '\n')
        T.insert(CURRENT, "Life Expec.:\t\t" + str(count.lifeExp) + '\n')
        T.insert(CURRENT, "Currency:\t\t" + count.currencyName + '\n')
        T.insert(CURRENT, "Currency 3 L.:\t\t" + count.currency3letter + '\n')
        T.insert(CURRENT, "GDP:\t\t" + str(count.gdp) + '\n')
        T.insert(CURRENT, "Inflation:\t\t" + str(count.inflation) + '\n')
        T.insert(CURRENT, "Tourism:\t\t" + str(count.tourism) + '\n')
        T.insert(CURRENT, "Currency Exch.:\t\t" + str(count.currencyExchange) + '\n')

    #Abre uma nova janela, listando o dado selecionado de maneira crescente ou decrescente
    def List_it(self, data, value):
        frame = tk.Toplevel(self)
        
        #Imprime o dado selecionado, tal como o usuario o digitou
        label = tk.Label(frame, text="%s" %(data))
        label.pack()
        
        #Seta scrollbar e text box
        S = tk.Scrollbar(frame)
        T = tk.Text(frame, height=10, width=50)
        S.pack(pady=2, padx=2, side=RIGHT)
        T.pack(pady=2, padx=2, side=LEFT)
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)

        #Padroniza a entrada
        data = unidecode(data)
        data = data.lower()
        data = data.split(' ')
        data = ''.join(data)
        
        lista = []
        
        #Inicializa a arvore B
        b = btree.BTree(4)
        nameoffile = "../data/Btrees/" + data + ".pkl"

        if not os.path.exists(nameoffile):
            T.insert(CURRENT, "There is no such data.\n")

        else:
            file = open(nameoffile, 'rb')
            b = pickle.load(file)
            file.close()
            
            #Estamos usando apenas a arvore B, uma vez que teriamos problemas com o Pickle
            #Teriamos que abrir e fechar o arquivo a cada pesquisa, pois ele eh um serializador
        
            if value == 0:
                lista = b.crescent(b._root, lista)
            else:
                lista = b.decrescent(b._root, lista)
            
            #For que imprime cada objeto da lista organizada
            for obj in lista:
                if obj[0] != 0:
                    T.insert(CURRENT, obj[1] + ' \t\t ' + str(obj[0]) + "\n")
                else:
                    T.insert(CURRENT, obj[1] + ' \t\t ' + 'n.a.' + "\n")

    #Abre uma nova janela que exibe simultaneamente os dados dos dois paises selecionados anteriormente
    def Compare(self, country1, country2):
        frame = tk.Toplevel(self)

        #Adicione '../' antes de Btrees, se esta numa pasta irma
        bname = open("../data/Btrees/names.pkl", 'rb')

        b = btree.BTree(4)
        b = pickle.load(bname)
        nodo = b.show([country1])
        ind1 = nodo[1]

        nodo = b.show([country2])
        ind2 = nodo[1]
        
        bname.close()

        #Como usamos um serializador, eh necessario verificar qual tem o menor indice.
        #Se isso nao for feito, ocorre um erro.
        if ind1 > ind2:
            aux = country1
            country1 = country2
            country2 = aux
            a = ind1
            ind1 = ind2
            ind2 = a
        
        #Exibe a string "#pais1 vs #pais2"
        label1 = tk.Label(frame, text="%s" %(country1), font=LARGE_FONT)
        label1.grid(row=0, column=2, sticky="E")

        labelvs = tk.Label(frame, text="vs", font=LARGE_FONT)
        labelvs.grid(row=0, column=3)

        label2 = tk.Label(frame, text="%s" %(country2), font=LARGE_FONT)
        label2.grid(row=0, column=4, sticky="W")

        #Adicione '../' antes de Btrees, se esta numa pasta irma
        binary = open("../data/Btrees/binaries.kbb", 'rb')
        for num in range(0, ind1):          #Busca, com base no indice, o bloco do pais solicitado
            count1 = pickle.load(binary)

        for num in range(0, ind2-ind1):
            count2 = pickle.load(binary)

        binary.close()
        
        #Seta o path para os mapas e bandeiras
        map1 = count1.return_path_map()
        map2 = count2.return_path_map()
        flag1 = count1.return_path_flag()
        flag2 = count2.return_path_flag()

        #Bandeira do pais 1
        #As primeiras tres linhas nos 4 casos sao para o tratamento da imagem
        im_temp = Image.open(flag1)
        im_temp = im_temp.resize((175, 90), Image.ANTIALIAS)
        im_temp.save("teste.gif", "gif")
        
        flag1 = tk.PhotoImage(file="teste.gif")
        painel11 = tk.Label(frame, image = flag1)
        painel11.image = flag1 #mantenha a referencia, mantenha a referencia, mantenha a refere...
        painel11.grid(row=1, column=1)

        #Mapa do pais 1
        im_temp = Image.open(map1)
        im_temp = im_temp.resize((175, 90), Image.ANTIALIAS)
        im_temp.save("teste.gif", "gif")
        
        map1 = tk.PhotoImage(file="teste.gif")
        painel1 = tk.Label(frame, image = map1)
        painel1.image = map1 #mantenha a referencia, mantenha a referencia, mantenha a refere...
        painel1.grid(row=1, column=2)

        #Bandeira do pais 2
        im_temp = Image.open(flag2)
        im_temp = im_temp.resize((175, 90), Image.ANTIALIAS)
        im_temp.save("teste.gif", "gif")
        
        flag2 = tk.PhotoImage(file="teste.gif")
        painel22 = tk.Label(frame, image = flag2)
        painel22.image = flag2 #mantenha a referencia, mantenha a referencia, mantenha a refere...
        painel22.grid(row=1, column=4)

        #Mapa do pais 2
        im_temp = Image.open(map2)
        im_temp = im_temp.resize((175, 90), Image.ANTIALIAS)
        im_temp.save("teste.gif", "gif")
        
        map2 = tk.PhotoImage(file="teste.gif")
        painel2 = tk.Label(frame, image = map2)
        painel2.image = map2 #mantenha a referencia, mantenha a referencia, mantenha a refere...
        painel2.grid(row=1, column=5)
        
        S1 = tk.Scrollbar(frame)
        T1 = tk.Text(frame, height=10, width=50)
        S1.grid(pady=2, padx=2, row=2, column=0)
        T1.grid(pady=2, padx=2, row=2, column=1, columnspan=2)
        
        S2 = tk.Scrollbar(frame)
        T2 = tk.Text(frame, height=10, width=50)
        S2.grid(pady=2, padx=2, row=2, column=6)
        T2.grid(pady=2, padx=2, row=2, column=4, columnspan=2)
        
        S1.config(command=T1.yview)
        T1.config(yscrollcommand=S1.set)
        S2.config(command=T2.yview)
        T2.config(yscrollcommand=S2.set)

        #Dados sao impressos de maneira ingenua (nao conseguimos desenvolver outra implementacao)

        T1.insert(CURRENT, "Capital:\t\t" + count1.capital + '\n')
        T2.insert(CURRENT, "Capital:\t\t" + count2.capital + '\n')

        T1.insert(CURRENT, "ISO3166a2:\t\t" + count1.iso3166a2 + '\n')
        T2.insert(CURRENT, "ISO3166a2:\t\t" + count2.iso3166a2 + '\n')

        T1.insert(CURRENT, "ISO3166a3:\t\t" + count1.iso3166a3 + '\n')
        T2.insert(CURRENT, "ISO3166a3:\t\t" + count2.iso3166a3 + '\n')

        T1.insert(CURRENT, "Internet TDL:\t\t" + count1.iso3166a2 + '\n')
        T2.insert(CURRENT, "Internet TDL:\t\t" + count2.iso3166a2 + '\n')

        T1.insert(CURRENT, "Calling Code:\t\t" + count1.iso3166a2 + '\n')
        T2.insert(CURRENT, "Calling Code:\t\t" + count2.iso3166a2 + '\n')

        T1.insert(CURRENT, "Continent:\t\t" + count1.continent + '\n')
        T2.insert(CURRENT, "Continent:\t\t" + count2.continent + '\n')

        T1.insert(CURRENT, "Government:\t\t" + count1.government + '\n')
        T2.insert(CURRENT, "Government:\t\t" + count2.government + '\n')

        T1.tag_config('destaque', font=('Courier', 9, 'bold'))
        T2.tag_config('destaque', font=('Courier', 9, 'bold'))

        if count1.population > count2.population:
            T1.insert(CURRENT, "Population:\t\t" + str(count1.population) + '\n', 'destaque')
            T2.insert(CURRENT, "Population:\t\t" + str(count2.population) + '\n')
        else:
            T1.insert(CURRENT, "Population:\t\t" + str(count1.population) + '\n')
            T2.insert(CURRENT, "Population:\t\t" + str(count2.population) + '\n', 'destaque')
        
        if count1.area > count2.area:
            T1.insert(CURRENT, "Area:\t\t" + str(count1.area) + '\n', 'destaque')
            T2.insert(CURRENT, "Area:\t\t" + str(count2.area) + '\n')
        else:
            T1.insert(CURRENT, "Area:\t\t" + str(count1.area) + '\n')
            T2.insert(CURRENT, "Area:\t\t" + str(count2.area) + '\n', 'destaque')

        if count1.coastArea > count2.coastArea:
            T1.insert(CURRENT, "Coast Area:\t\t" + str(count1.coastArea) + '\n', 'destaque')
            T2.insert(CURRENT, "Coast Area:\t\t" + str(count2.coastArea) + '\n')
        else:
            T1.insert(CURRENT, "Coast Area:\t\t" + str(count1.coastArea) + '\n')
            T2.insert(CURRENT, "Coast Area:\t\t" + str(count2.coastArea) + '\n', 'destaque')

        if count1.hdi > count2.hdi:
            T1.insert(CURRENT, "HDI:\t\t" + str(count1.hdi) + '\n', 'destaque')
            T2.insert(CURRENT, "HDI:\t\t" + str(count2.hdi) + '\n')
        else:
            T1.insert(CURRENT, "HDI:\t\t" + str(count1.hdi) + '\n')
            T2.insert(CURRENT, "HDI:\t\t" + str(count2.hdi) + '\n', 'destaque')

        if count1.gini < count2.gini:
            T1.insert(CURRENT, "GINI:\t\t" + str(count1.gini) + '\n', 'destaque')
            T2.insert(CURRENT, "GINI:\t\t" + str(count2.gini) + '\n')
        else:
            T1.insert(CURRENT, "GINI:\t\t" + str(count1.gini) + '\n')
            T2.insert(CURRENT, "GINI:\t\t" + str(count2.gini) + '\n', 'destaque')

        if count1.lifeExp > count2.lifeExp:
            T1.insert(CURRENT, "Life Expectancy:\t\t" + str(count1.lifeExp) + '\n', 'destaque')
            T2.insert(CURRENT, "Life Expectancy:\t\t" + str(count2.lifeExp) + '\n')
        else:
            T1.insert(CURRENT, "Life Expect.:\t\t" + str(count1.lifeExp) + '\n')
            T2.insert(CURRENT, "Life Expect.:\t\t" + str(count2.lifeExp) + '\n', 'destaque')

        T1.insert(CURRENT, "Currency:\t\t" + count1.currencyName + '\n')
        T2.insert(CURRENT, "Currency:\t\t" + count2.currencyName + '\n')

        T1.insert(CURRENT, "Currency 3 L:\t\t" + count1.currency3letter + '\n')
        T2.insert(CURRENT, "Currency 3 L:\t\t" + count2.currency3letter + '\n')

        if count1.gdp > count2.gdp:
            T1.insert(CURRENT, "GDP:\t\t" + str(count1.gdp) + '\n', 'destaque')
            T2.insert(CURRENT, "GDP:\t\t" + str(count2.gdp) + '\n')
        else:
            T1.insert(CURRENT, "GDP:\t\t" + str(count1.gdp) + '\n')
            T2.insert(CURRENT, "GDP:\t\t" + str(count2.gdp) + '\n', 'destaque')

        if count1.inflation < count2.inflation:
            T1.insert(CURRENT, "Inflation:\t\t" + str(count1.inflation) + '\n', 'destaque')
            T2.insert(CURRENT, "Inflation:\t\t" + str(count2.inflation) + '\n')
        else:
            T1.insert(CURRENT, "Inflation:\t\t" + str(count1.inflation) + '\n')
            T2.insert(CURRENT, "Inflation:\t\t" + str(count2.inflation) + '\n', 'destaque')

        if count1.tourism > count2.tourism:
            T1.insert(CURRENT, "Tourism:\t\t" + str(count1.tourism) + '\n', 'destaque')
            T2.insert(CURRENT, "Tourism:\t\t" + str(count2.tourism) + '\n')
        else:
            T1.insert(CURRENT, "Tourism:\t\t" + str(count1.tourism) + '\n')
            T2.insert(CURRENT, "Tourism:\t\t" + str(count2.tourism) + '\n', 'destaque')

        if count1.currencyExchange < count2.currencyExchange:
            T1.insert(CURRENT, "Currency Exch.:\t\t" + str(count1.currencyExchange) + '\n', 'destaque')
            T2.insert(CURRENT, "Currency Exch.:\t\t" + str(count2.currencyExchange) + '\n')
        else:
            T1.insert(CURRENT, "Currency Exch.:\t\t" + str(count1.currencyExchange) + '\n')
            T2.insert(CURRENT, "Currency Exch.:\t\t" + str(count2.currencyExchange) + '\n', 'destaque')

#Pagina inicial e principal
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Select", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        #Botao que leva a janela de exibicao
        button1 = tk.Button(self, text="Display",
                            command=lambda: controller.show_frame(SelExibe),
                            height = 1, width = 10)
        button1.pack(pady=5)

        #Botao que leva a janela de listagem
        button2 = tk.Button(self, text="Listing",
                            command=lambda: controller.show_frame(SelLista),
                            height = 1, width = 10)
        button2.pack(pady=5)

        #Botao que leva a janela de comparacao
        button3 = tk.Button(self, text="Comparison",
                            command=lambda: controller.show_frame(SelCompara),
                            height = 1, width = 10)
        button3.pack(pady=5)
        
        #Botao de encerramento
        button4 = tk.Button(self, text="Quit",
                            command=lambda: controller.quit_it(),
                            height = 1, width=10)
        button4.pack(pady=10)

#Frame secundario, onde o usuario seleciona qual pais quer exibir
class SelExibe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Select the country to be displayed", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        l1 = tk.Label(self, text="Country: ")
        l1.pack()

        e1 = tk.Entry(self)
        e1.pack()

        #Botao de busca: inicializa uma nova janela onde o pais sera exibido
        button1 = tk.Button(self, text="Search", command=lambda: controller.Display(e1.get()))
        button1.pack(pady=20)
        
        #Botao para voltar para a StartPage
        button2 = tk.Button(self, text="Back", command=lambda:controller.show_frame(StartPage),
                            heigh = 1, width = 10)
        button2.pack(pady=10, padx=10, side=LEFT)

#Frame onde o usuario selecionara qual dado quer listar e de que maneira quer faze-lo (crescente ou decrescente)
class SelLista(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        var = tk.IntVar()
        
        label = tk.Label(self, text="Select the data to be listed", font=LARGE_FONT)
        label.pack(pady=10)

        l1 = tk.Label(self, text="Data: ")
        l1.pack()

        e1 = tk.Entry(self)
        e1.pack(pady=10)

        radiob1 = tk.Radiobutton(self, text="Crescent Order", variable=var, value=0)
        radiob1.pack()

        radiob2 = tk.Radiobutton(self, text="Decrescent Order", variable=var, value=1)
        radiob2.pack()

        button1 = tk.Button(self, text="Search", command=lambda: controller.List_it(e1.get(), var.get()))
        button1.pack(pady=10)
        
        button2 = tk.Button(self, text="Back", command=lambda:controller.show_frame(StartPage),
                            heigh = 1, width = 10)
        button2.pack(pady=10, padx=10, side=LEFT)

#Frame em que o usuario selecionara dois paises para serem comparados
class SelCompara(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Select the countries to be compared", font=LARGE_FONT)
        label.grid(column=0, columnspan=3, padx=20)

        l1 = tk.Label(self, text="Country 1:")
        e1 = tk.Entry(self, width=30)
        l1.grid(pady=10, padx=10, row=1, column=0)
        e1.grid(pady=10, padx=10, row=1, column=2, columnspan=2)
        
        l2 = tk.Label(self, text="Country 2:")
        e2 = tk.Entry(self, width=30)
        l2.grid(pady=10, padx=10, row=2, column=0)
        e2.grid(pady=10, padx=10, row=2, column=2, columnspan=2)

        button1 = tk.Button(self, text="Search", command=lambda: controller.Compare(e1.get(), e2.get()),
                            height = 1, width = 10)
        button1.grid(column=1, columnspan=2, pady=20)
        
        button2 = tk.Button(self, text="Back", command=lambda:controller.show_frame(StartPage),
                            heigh = 1, width = 10)
        button2.grid(column=0, padx=10, pady=10)
