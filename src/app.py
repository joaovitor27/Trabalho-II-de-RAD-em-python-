import tkinter
from tkinter import ttk, messagebox
from tkinter.ttk import Scrollbar

from src.database import get_pessoas, get_contas, get_funcionarios, get_pessoa, get_conta, get_employee, \
    insert_pessoa, insert_conta, insert_employee

LARGEFONT = ("Verdana", 35)


class TkinterApp(tkinter.Tk):

    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)

        container = tkinter.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for f in (StartPage, Page1, Page2, Page3, Page4, Page5, Page6, Page7, Page8, Page9):
            frame = f(container, self)
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


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

    def exibe(self):
        messagebox.showinfo('Resultado da Busca: ', 'Resultado: ' + str(get_employee(int(self.entrada.get()))))


class Page7(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        self.label_cpf = tkinter.Label(self, text='Digite o CPF:')
        self.label_cpf.grid(row=1, column=1, padx=10, pady=10)

        self.entrada_cpf = tkinter.Entry(self, width=30)
        self.entrada_cpf.grid(row=1, column=2, padx=10, pady=10)

        self.label_first_name = tkinter.Label(self, text='Digite o primeiro Nome:')
        self.label_first_name.grid(row=2, column=1, padx=10, pady=10)

        self.entrada_first_name = tkinter.Entry(self, width=30)
        self.entrada_first_name.grid(row=2, column=2, padx=10, pady=10)

        self.label_middle_name = tkinter.Label(self, text='Digite o nome do meio:')
        self.label_middle_name.grid(row=3, column=1, padx=10, pady=10)

        self.entrada_middle_name = tkinter.Entry(self, width=30)
        self.entrada_middle_name.grid(row=3, column=2, padx=10, pady=10)

        self.label_last_name = tkinter.Label(self, text='Digite o último nome:')
        self.label_last_name.grid(row=4, column=1, padx=10, pady=10)

        self.entrada_last_name = tkinter.Entry(self, width=30)
        self.entrada_last_name.grid(row=4, column=2, padx=10, pady=10)

        self.label_age = tkinter.Label(self, text='Digite a idade:')
        self.label_age.grid(row=5, column=1, padx=10, pady=10)

        self.entrada_age = tkinter.Entry(self, width=30)
        self.entrada_age.grid(row=5, column=2, padx=10, pady=10)

        self.label_email = tkinter.Label(self, text='Digite o email:')
        self.label_email.grid(row=7, column=1, padx=10, pady=10)

        self.entrada_email = tkinter.Entry(self, width=30)
        self.entrada_email.grid(row=7, column=2, padx=10, pady=10)

        self.botao = tkinter.Button(self, text='Enserir', command=self.insert)
        self.botao_sair = tkinter.Button(self, text='voltar', command=lambda: controller.show_frame(StartPage))

        self.botao.grid(row=8, column=3, padx=10, pady=10)
        self.botao_sair.grid(row=8, column=4, padx=10, pady=10)

    def insert(self):
        resut = insert_pessoa(self.entrada_cpf.get(), self.entrada_first_name.get(), self.entrada_middle_name.get(),
                              self.entrada_last_name.get(), int(self.entrada_age.get()), self.entrada_email.get())

        messagebox.showinfo('Resultado da Busca: ', f'{resut}')


class Page8(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        self.label_agency = tkinter.Label(self, text='Digite a Agência: (0000-0)')
        self.label_agency.grid(row=1, column=1, padx=10, pady=10)

        self.entrada_agency = tkinter.Entry(self, width=30)
        self.entrada_agency.grid(row=1, column=2, padx=10, pady=10)

        self.label_number_conta = tkinter.Label(self, text='Digite o número da conta: (00000-0)')
        self.label_number_conta.grid(row=2, column=1, padx=10, pady=10)

        self.entrada_number_conta = tkinter.Entry(self, width=30)
        self.entrada_number_conta.grid(row=2, column=2, padx=10, pady=10)

        self.label_saldo = tkinter.Label(self, text='Digite o Saldo da conta')
        self.label_saldo.grid(row=3, column=1, padx=10, pady=10)

        self.entrada_saldo = tkinter.Entry(self, width=30)
        self.entrada_saldo.grid(row=3, column=2, padx=10, pady=10)

        self.label_id_gerente = tkinter.Label(self, text='Digite o id do gerente')
        self.label_id_gerente.grid(row=4, column=1, padx=10, pady=10)

        self.entrada_id_gerente = tkinter.Entry(self, width=30)
        self.entrada_id_gerente.grid(row=4, column=2, padx=10, pady=10)

        self.label_id_pessoa = tkinter.Label(self, text='Digite o id da pessoa')
        self.label_id_pessoa.grid(row=5, column=1, padx=10, pady=10)

        self.entrada_id_pessoa = tkinter.Entry(self, width=30)
        self.entrada_id_pessoa.grid(row=5, column=2, padx=10, pady=10)

        self.botao = tkinter.Button(self, text='Enserir', command=self.insert)
        self.botao_sair = tkinter.Button(self, text='voltar', command=lambda: controller.show_frame(StartPage))

        self.botao.grid(row=6, column=3, padx=10, pady=10)
        self.botao_sair.grid(row=6, column=4, padx=10, pady=10)

    def insert(self):
        saldo = self.entrada_saldo.get()
        if ',' in saldo:
            saldo = saldo.replace(',', '.')
        saldo = float(saldo)
        resut = insert_conta(self.entrada_agency.get(), self.entrada_number_conta.get(), saldo,
                             int(self.entrada_id_gerente.get()), int(self.entrada_id_pessoa.get()))

        messagebox.showinfo('Resultado da Busca: ', f'{resut}')


class Page9(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        self.label_office = tkinter.Label(self, text='Digite o cargo:')
        self.label_office.grid(row=1, column=1, padx=10, pady=10)

        self.entrada_office = tkinter.Entry(self, width=30)
        self.entrada_office.grid(row=1, column=2, padx=10, pady=10)

        self.label_wage = tkinter.Label(self, text='Digite o salário')
        self.label_wage.grid(row=2, column=1, padx=10, pady=10)

        self.entrada_wage = tkinter.Entry(self, width=30)
        self.entrada_wage.grid(row=2, column=2, padx=10, pady=10)

        self.label_id_pessoa = tkinter.Label(self, text='Digite o id da pessoa')
        self.label_id_pessoa.grid(row=3, column=1, padx=10, pady=10)

        self.entrada_id_pessoa = tkinter.Entry(self, width=30)
        self.entrada_id_pessoa.grid(row=3, column=2, padx=10, pady=10)

        self.botao = tkinter.Button(self, text='Enserir', command=self.insert)
        self.botao_sair = tkinter.Button(self, text='voltar', command=lambda: controller.show_frame(StartPage))

        self.botao.grid(row=4, column=3, padx=10, pady=10)
        self.botao_sair.grid(row=4, column=4, padx=10, pady=10)

    def insert(self):
        wage = self.entrada_wage.get()
        if ',' in wage:
            wage = wage.replace(',', '.')
        wage = float(wage)
        resut = insert_employee(self.entrada_office.get(), wage, int(self.entrada_id_pessoa.get()))

        messagebox.showinfo('Resultado da Busca: ', f'{resut}')


app = TkinterApp()
app.mainloop()
