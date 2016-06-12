#improved GUI
#Corrijam meu ingles, senpais.
#Se quiserem rodar essa GUI, baixem o Pillow e o Unidecode

import tkinter as tk
from tkinter import END, LEFT, RIGHT
from PIL import Image
from unidecode import unidecode
import pycountry

dictio = {}
t = list(pycountry.countries)
for country in t:
    name = country.name.lower()
    name = unidecode(name)
    iso = country.alpha3
    dictio[name] = iso

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

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def Display(self, country):
        frame = tk.Toplevel(self)
        label = tk.Label(frame, text="%s" %(country))
        label.pack()
        S = tk.Scrollbar(frame)
        T = tk.Text(frame, height=4, width=50)
        S.pack(pady=2, padx=2, side=RIGHT)
        T.pack(pady=2, padx=2, side=LEFT)
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)
        quote="""Aqui serao exibidos os dados de um pais"""
        T.insert(END, quote)

    def List(self, data):
        frame = tk.Toplevel(self)
        label = tk.Label(frame, text="%s" %(data))
        label.pack()
        S = tk.Scrollbar(frame)
        T = tk.Text(frame, height=4, width=50)
        S.pack(pady=2, padx=2, side=RIGHT)
        T.pack(pady=2, padx=2, side=LEFT)
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)
        quote="""Aqui serao exibidos os dados de maneira crescente ou decrescente"""
        T.insert(END, quote)

    def Compare(self, country1, country2):
        frame = tk.Toplevel(self)
        label1 = tk.Label(frame, text="%s vs %s" %(country1, country2))
        label1.grid(row=0, column=3)
    
        country1 = country1.lower()
        country1 = unidecode(country1)

        country2 = country2.lower()
        country2 = unidecode(country2)
        
        alpha1 = dictio[country1]
        alpha2 = dictio[country2]

        #Bandeira do pais 1
        im_temp = Image.open("Flags/"+alpha1+".gif")
        im_temp = im_temp.resize((175, 88), Image.ANTIALIAS)
        im_temp.save("teste.gif", "gif")
        
        flag1 = tk.PhotoImage(file="teste.gif")
        painel11 = tk.Label(frame, image = flag1)
        painel11.image = flag1 #mantenha a referencia, mantenha a referencia, mantenha a refere...
        painel11.grid(row=1, column=1)

        #Mapa do pais 1
        im_temp = Image.open("Maps/"+alpha1+".gif")
        im_temp = im_temp.resize((175, 88), Image.ANTIALIAS)
        im_temp.save("teste.gif", "gif")
        
        map1 = tk.PhotoImage(file="teste.gif")
        painel1 = tk.Label(frame, image = map1)
        painel1.image = map1 #mantenha a referencia, mantenha a referencia, mantenha a refere...
        painel1.grid(row=1, column=2)

        #Bandeira do pais 2
        im_temp = Image.open("Flags/"+alpha2+".gif")
        im_temp = im_temp.resize((175, 88), Image.ANTIALIAS)
        im_temp.save("teste.gif", "gif")
        
        flag2 = tk.PhotoImage(file="teste.gif")
        painel22 = tk.Label(frame, image = flag2)
        painel22.image = flag2 #mantenha a referencia, mantenha a referencia, mantenha a refere...
        painel22.grid(row=1, column=4)

        #Mapa do pais 2
        im_temp = Image.open("Maps/"+alpha2+".gif")
        im_temp = im_temp.resize((175, 88), Image.ANTIALIAS)
        im_temp.save("teste.gif", "gif")
        
        map2 = tk.PhotoImage(file="teste.gif")
        painel2 = tk.Label(frame, image = map2)
        painel2.image = map2 #mantenha a referencia, mantenha a referencia, mantenha a refere...
        painel2.grid(row=1, column=5)
        
        S1 = tk.Scrollbar(frame)
        T1 = tk.Text(frame, height=4, width=50)
        S1.grid(pady=2, padx=2, row=2, column=0)
        T1.grid(pady=2, padx=2, row=2, column=1, columnspan=2)
        
        S2 = tk.Scrollbar(frame)
        T2 = tk.Text(frame, height=4, width=50)
        S2.grid(pady=2, padx=2, row=2, column=6)
        T2.grid(pady=2, padx=2, row=2, column=4, columnspan=2)
        
        S1.config(command=T1.yview)
        T1.config(yscrollcommand=S1.set)
        S2.config(command=T2.yview)
        T2.config(yscrollcommand=S2.set)
        quote="Aqui serao exibidos os dados do pais #"
        T1.insert(END, quote + country1)
        T2.insert(END, quote + country2)

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Select", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Display",
                            command=lambda: controller.show_frame(SelExibe),
                            height = 1, width = 10)
        button1.pack(pady=5)

        button2 = tk.Button(self, text="Listing",
                            command=lambda: controller.show_frame(SelLista),
                            height = 1, width = 10)
        button2.pack(pady=5)

        button3 = tk.Button(self, text="Comparison",
                            command=lambda: controller.show_frame(SelCompara),
                            height = 1, width = 10)
        button3.pack(pady=5)

class SelExibe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Select the country to be displayed", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        l1 = tk.Label(self, text="Country: ")
        l1.pack()

        e1 = tk.Entry(self)
        e1.pack()

        button1 = tk.Button(self, text="Search", command=lambda: controller.Display(e1.get()))
        button1.pack(pady=20)

class SelLista(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Select the data to be listed", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        l1 = tk.Label(self, text="Data: ")
        l1.pack()

        e1 = tk.Entry(self)
        e1.pack()

        button1 = tk.Button(self, text="Search", command=lambda: controller.List(e1.get()))
        button1.pack(pady=20)

class SelCompara(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Select the countries to be compared", font=LARGE_FONT)
        label.grid(column=0, columnspan=3, padx=20)

        l1 = tk.Label(self, text="Country 1: ")
        e1 = tk.Entry(self)
        l1.grid(pady=10, padx=10, row=1, column=0)
        e1.grid(pady=10, padx=10, row=1, column=1, columnspan=2)
        
        l2 = tk.Label(self, text="Country 2: ")
        e2 = tk.Entry(self)
        l2.grid(pady=10, padx=10, row=2, column=0)
        e2.grid(pady=10, padx=10, row=2, column=1, columnspan=2)

        button1 = tk.Button(self, text="Search", command=lambda: controller.Compare(e1.get(), e2.get()),
                            height = 1, width = 10)
        button1.grid(column=0, columnspan=2, pady=20)

app = App()
app.title("Remove Kebab")
app.mainloop()
