#improved GUI
#Corrijam meu ingles, senpais.

import Tkinter as tk
from Tkinter import END, LEFT, RIGHT

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
        label = tk.Label(frame, text="%s and %s" %(country1, country2))
        label.pack()
        S1 = tk.Scrollbar(frame)
        T1 = tk.Text(frame, height=4, width=25)
        S1.pack(pady=2, padx=2, side=LEFT)
        T1.pack(pady=2, padx=2, side=LEFT)
        S2 = tk.Scrollbar(frame)
        T2 = tk.Text(frame, height=4, width=25)
        S2.pack(pady=2, padx=2, side=RIGHT)
        T2.pack(pady=2, padx=2, side=RIGHT)
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
