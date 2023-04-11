from tkinter import *
from tkinter import ttk
from create import criar_filmes, criar_user

janela = Tk()


class Aplicacao():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames()
        self.botoes()
        self.labels()
        self.inputs()
        self.lista_frame2()
        self.insert_user()
        janela.mainloop()

    def tela(self):
        self.janela.title('Seaflix')
        self.janela.geometry('700x600')
        self.janela.iconbitmap('sea.ico')
        self.janela.configure(background='#0591af')
        self.janela.resizable(True, True)
        self.janela.maxsize(width=700, height=600)

    def frames(self):
        self.frame_0 = Frame(self.janela, bg='#ceebf2', highlightthickness=1, highlightbackground='#011013')
        self.frame_0.place(relx=0.03, rely=0.03, relwidth=0.94, relheight=0.11)

        self.frame_1 = Frame(self.janela, bg='#ceebf2', highlightthickness=1, highlightbackground='#011013')
        self.frame_1.place(relx=0.03, rely=0.2, relwidth=0.94, relheight=0.35)

        self.frame_2 = Frame(self.janela, bg='#ceebf2', highlightthickness=1, highlightbackground='#011013')
        self.frame_2.place(relx=0.03, rely=0.6, relwidth=0.94, relheight=0.38)

    def botoes(self):
        self.btBuscar = Button(self.frame_0, text='Buscar', fg='#fff', bg='#011013', relief='flat')
        self.btBuscar.place(relx=0.15, rely=0.25, relwidth=0.1, relheight=0.5)

        self.btLimpar = Button(self.frame_0, text='Limpar', fg='#fff', bg='#011013', relief='flat')
        self.btLimpar.place(relx=0.28, rely=0.25, relwidth=0.1, relheight=0.5)

        self.btCreate = Button(self.frame_0, text='Criar', fg='#fff', bg='#011013', relief='flat')
        self.btCreate.place(relx=0.45, rely=0.25, relwidth=0.1, relheight=0.5)

        self.btRead = Button(self.frame_0, text='Listar', fg='#fff', bg='#011013', relief='flat')
        self.btRead.place(relx=0.57, rely=0.25, relwidth=0.1, relheight=0.5)

        self.btUpdate = Button(self.frame_0, text='Atualizar', fg='#fff', bg='#011013', relief='flat')
        self.btUpdate.place(relx=0.70, rely=0.25, relwidth=0.1, relheight=0.5)

        self.btDelete = Button(self.frame_0, text='Deletar', fg='#fff', bg='#011013', relief='flat')
        self.btDelete.place(relx=0.82, rely=0.25, relwidth=0.1, relheight=0.5)

    def labels(self):
        self.lbIDUsuario = Label(self.frame_0, text='ID', bg='#ceebf2')
        self.lbIDUsuario.place(relx=0.005, rely=0.01, relwidth=0.1, relheight=0.3)

        self.lbIDNome = Label(self.frame_1, text='Nome:', bg='#ceebf2')
        self.lbIDNome.place(relx=0.005, rely=0.05, relwidth=0.1, relheight=0.15)

        self.lbIDEmail = Label(self.frame_1, text='E-Mail:', bg='#ceebf2')
        self.lbIDEmail.place(relx=0.005, rely=0.25, relwidth=0.1, relheight=0.15)

        self.lbIDPlano = Label(self.frame_1, text='Plano:', bg='#ceebf2')
        self.lbIDPlano.place(relx=0.005, rely=0.45, relwidth=0.1, relheight=0.15)

        self.lbIDTipo = Label(self.frame_1, text='Tipo:', bg='#ceebf2')
        self.lbIDTipo.place(relx=0.35, rely=0.45, relwidth=0.1, relheight=0.15)

        self.lbIDIdade = Label(self.frame_1, text='Idade:', bg='#ceebf2')
        self.lbIDIdade.place(relx=0.675, rely=0.45, relwidth=0.1, relheight=0.15)

    def inputs(self):
        self.inpIDUsuario = Entry(self.frame_0)
        self.inpIDUsuario.place(relx=0.005, rely=0.45, relwidth=0.1, relheight=0.5)

        self.inpNome = Entry(self.frame_1)
        self.inpNome.place(relx=0.12, rely=0.05, relwidth=0.8, relheight=0.15)

        self.inpEmail = Entry(self.frame_1)
        self.inpEmail.place(relx=0.12, rely=0.25, relwidth=0.8, relheight=0.15)

        self.inpPlano = Entry(self.frame_1)
        self.inpPlano.place(relx=0.12, rely=0.45, relwidth=0.2, relheight=0.15)

        self.inpTipo = Entry(self.frame_1)
        self.inpTipo.place(relx=0.44, rely=0.45, relwidth=0.2, relheight=0.15)

        self.inpIdade = Entry(self.frame_1)
        self.inpIdade.place(relx=0.77, rely=0.45, relwidth=0.15, relheight=0.15)

    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height=3, columns=('col1',
                                                                      'col2',
                                                                      'col3',
                                                                      'col4',
                                                                      'col5',
                                                                      'col6'))
        self.listaCli.heading('#0', text='ID')
        self.listaCli.heading('#1', text='Nome')
        self.listaCli.heading('#2', text='E-Mail')
        self.listaCli.heading('#3', text='Plano')
        self.listaCli.heading('#4', text='Tipo')
        self.listaCli.heading('#5', text='Idade')

        self.listaCli.column('#0', width=15)
        self.listaCli.column('#1', width=210)
        self.listaCli.column('#2', width=213)
        self.listaCli.column('#3', width=65)
        self.listaCli.column('#4', width=65)
        self.listaCli.column('#5', width=50)

        self.listaCli.place(relx=0.025, rely=0.05, relwidth=0.95, relheight=0.90)

    def insert_user(self):
        criar_user(self.inpNome.get(),
                   self.inpIdade.get(),
                   self.inpEmail.get(),
                   self.inpPlano.get(),
                   self.inpTipo.get())
