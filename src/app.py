import tkinter
from tkinter import ttk, messagebox
from tkinter.ttk import Scrollbar

from src.database import get_pessoas, get_contas, get_funcionarios, get_pessoa, get_conta, get_employee

LARGEFONT = ("Verdana", 35)


class TkinterApp(tkinter.Tk):

    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)

        container = tkinter.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for f in (StartPage, Page1, Page2, Page3, Page4, Page5, Page6):
            frame = f(container, self)
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Page7:
    pass


class Page8:
    pass


class Page9:
    pass


class Page10:
    pass


class Page11:
    pass


class Page12:
    pass


class Page13:
    pass


class Page14:
    pass


class Page15:
    pass


class StartPage(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Bem Vindo ao banco JV", font=LARGEFONT)
        label.grid(row=0, column=2, padx=10, pady=10)

        button1 = ttk.Button(self, text="Listar Pessoas", command=lambda: controller.show_frame(Page1))
        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="Listar Contas", command=lambda: controller.show_frame(Page2))
        button2.grid(row=1, column=2, padx=10, pady=10)

        button3 = ttk.Button(self, text="Listar Funcionários", command=lambda: controller.show_frame(Page3))
        button3.grid(row=1, column=3, padx=10, pady=10)

        button4 = ttk.Button(self, text="Buscar pessoa", command=lambda: controller.show_frame(Page4))
        button4.grid(row=2, column=1, padx=10, pady=10)

        button5 = ttk.Button(self, text="Buscar conta", command=lambda: controller.show_frame(Page5))
        button5.grid(row=2, column=2, padx=10, pady=10)

        button6 = ttk.Button(self, text="Buscar Funcionários", command=lambda: controller.show_frame(Page6))
        button6.grid(row=2, column=3, padx=10, pady=10)

        button7 = ttk.Button(self, text="Inserir pessoa", command=lambda: controller.show_frame(Page7))
        button7.grid(row=3, column=1, padx=10, pady=10)

        button8 = ttk.Button(self, text="Inserir conta", command=lambda: controller.show_frame(Page8))
        button8.grid(row=3, column=2, padx=10, pady=10)

        button9 = ttk.Button(self, text="Inserir Funcionários", command=lambda: controller.show_frame(Page9))
        button9.grid(row=3, column=3, padx=10, pady=10)

        button10 = ttk.Button(self, text="Deletar pessoa", command=lambda: controller.show_frame(Page10))
        button10.grid(row=4, column=1, padx=10, pady=10)

        button11 = ttk.Button(self, text="Deletar conta", command=lambda: controller.show_frame(Page11))
        button11.grid(row=4, column=2, padx=10, pady=10)

        button12 = ttk.Button(self, text="Deletar Funcionários", command=lambda: controller.show_frame(Page12))
        button12.grid(row=4, column=3, padx=10, pady=10)

        button13 = ttk.Button(self, text="Editar pessoa", command=lambda: controller.show_frame(Page13))
        button13.grid(row=5, column=1, padx=10, pady=10)

        button14 = ttk.Button(self, text="Editar conta", command=lambda: controller.show_frame(Page14))
        button14.grid(row=5, column=2, padx=10, pady=10)

        button14 = ttk.Button(self, text="Editar Funcionários", command=lambda: controller.show_frame(Page15))
        button14.grid(row=5, column=3, padx=10, pady=10)


class Page1(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Lista de pessoas", font=LARGEFONT)
        label.grid(row=1, column=1, padx=10, pady=10)
        
        pessoas = get_pessoas()
        scrollbar = Scrollbar(self)
        scrollbar.grid(row=2, column=1, padx=10, pady=10)

        mylist = tkinter.Listbox(self, yscrollcommand=scrollbar.set, width=100)
        for line in pessoas:
            mylist.insert(line[0], line[1] + " | " + line[2] + " | " + line[3] + " | " + line[4])

        mylist.grid(row=2, column=1, padx=50, pady=50)
        scrollbar.config(command=mylist.yview)

        button1 = ttk.Button(self, text="Voltar", command=lambda: controller.show_frame(StartPage))
        button1.grid(row=3, column=1, padx=10, pady=10)


class Page2(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Lista de Contas", font=LARGEFONT)
        label.grid(row=1, column=1, padx=10, pady=10)

        contas = get_contas()
        scrollbar = Scrollbar(self)
        scrollbar.grid(row=2, column=1, padx=10, pady=10)

        mylist = tkinter.Listbox(self, yscrollcommand=scrollbar.set, width=100)
        for line in contas:
            mylist.insert(line[0],
                          f'{line[1]} | {line[2]} | {str(line[3])} | {str(line[4])} | Dono da conta: {str(line[5])}')

        mylist.grid(row=2, column=1, padx=50, pady=50)
        scrollbar.config(command=mylist.yview)

        button1 = ttk.Button(self, text="Voltar", command=lambda: controller.show_frame(StartPage))
        button1.grid(row=3, column=1, padx=10, pady=10)


class Page3(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Lista de Funcionários", font=LARGEFONT)
        label.grid(row=1, column=1, padx=10, pady=10)

        employee = get_funcionarios()
        scrollbar = Scrollbar(self)
        scrollbar.grid(row=2, column=1, padx=10, pady=10)

        mylist = tkinter.Listbox(self, yscrollcommand=scrollbar.set, width=100)
        for line in employee:
            mylist.insert(line[0],
                          f'{line[1]} | {str(line[2])} | {str(line[4])} | Funcionário: {str(line[3])}')

        mylist.grid(row=2, column=1, padx=50, pady=50)
        scrollbar.config(command=mylist.yview)

        button1 = ttk.Button(self, text="Voltar", command=lambda: controller.show_frame(StartPage))
        button1.grid(row=3, column=1, padx=10, pady=10)


class Page4(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)

        self.label = tkinter.Label(self, text='Digite o CPF da pessoa (sem ponto e traço):')
        self.entrada = tkinter.Entry(self, width=30)

        self.label.pack(side='left')
        self.entrada.pack(side='left')

        self.botao = tkinter.Button(self, text='Exibir', command=self.exibe)
        self.botao_sair = tkinter.Button(self, text='voltar', command=lambda: controller.show_frame(StartPage))

        self.botao.pack(side='left')
        self.botao_sair.pack(side='left')

        self.botao.pack()
        self.botao_sair.pack()

    def exibe(self):
        messagebox.showinfo('Resultado da Busca', 'Resultado: ' + str(get_pessoa(self.entrada.get())))


class Page5(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)

        self.label = tkinter.Label(self, text='Digite o número da conta (00000-0):')
        self.entrada = tkinter.Entry(self, width=30)

        self.label.pack(side='left')
        self.entrada.pack(side='left')

        self.botao = tkinter.Button(self, text='Exibir', command=self.exibe)
        self.botao_sair = tkinter.Button(self, text='voltar', command=lambda: controller.show_frame(StartPage))

        self.botao.pack(side='left')
        self.botao_sair.pack(side='left')

        self.botao.pack()
        self.botao_sair.pack()

    def exibe(self):
        messagebox.showinfo('Resultado da Busca', 'Resultado: ' + str(get_conta(self.entrada.get())))


class Page6(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)

        self.label = tkinter.Label(self, text='Digite o id do funcionário:')
        self.entrada = tkinter.Entry(self, width=30)

        self.label.pack(side='left')
        self.entrada.pack(side='left')

        self.botao = tkinter.Button(self, text='Exibir', command=self.exibe)
        self.botao_sair = tkinter.Button(self, text='voltar', command=lambda: controller.show_frame(StartPage))

        self.botao.pack(side='left')
        self.botao_sair.pack(side='left')

        self.botao.pack()
        self.botao_sair.pack()

    def exibe(self):
        messagebox.showinfo('Resultado da Busca: ', 'Resultado: ' + str(get_employee(int(self.entrada.get()))))


app = TkinterApp()
app.mainloop()
