import tkinter as tk

LARGE_FONT = ("Verdana", 12)

class Aplicativo(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Exibe, Lista, Compara): #itera entre os frames pricipais

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):    #frame inicial
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Selecione uma forma de busca", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Exibição",
                            command=lambda: controller.show_frame(Exibe),
                            height = 1, width = 10)
        button1.pack()

        button2 = tk.Button(self, text="Listagem",
                            command=lambda: controller.show_frame(Lista),
                            height = 1, width = 10)
        button2.pack()

        button1 = tk.Button(self, text="Comparação",
                            command=lambda: controller.show_frame(Compara),
                            height = 1, width = 10)
        button1.pack()

class Exibe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Selecione o país a ser exibido", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        l1 = tk.Label(self, text="País: ")
        l1.pack()

        e1 = tk.Entry(self)
        e1.pack()

        button1 = tk.Button(self, text="Busca")
        button1.pack()

class Lista(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Selecione o dado a ser listado", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        l1 = tk.Label(self, text="Dado: ")
        l1.pack()

        e1 = tk.Entry(self)
        e1.pack()

        button1 = tk.Button(self, text="Busca")
        button1.pack()

class Compara(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Selecione os países a serem comparados", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        l1 = tk.Label(self, text="País 1: ")
        l1.pack()
        e1 = tk.Entry(self)
        e1.pack()
        
        l2 = tk.Label(self, text="País 2: ")
        l2.pack()     
        e2 = tk.Entry(self)
        e2.pack()

        button1 = tk.Button(self, text="Busca")
        button1.pack()

app = Aplicativo()
app.title("Remove Kebab")
app.mainloop()
