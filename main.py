from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox

#CORES
co0 = "#2F4F4F"  # VERDE ESCURO
co1 =  "#F0F8FF" # ALICE BLUE AZUL CLARO
co2 = "#363636" # CINZA MAIS ESCURO
co3 =  "#f0ffff" # AZURE BEM CLARO
co4 = "#FFFFFF" # BRANCO


# CRIANDO JANELA________________________________________________________
janela = Tk()
janela.title('')
janela.geometry('310x300')
janela.configure(background=co3)
janela.resizable(width=FALSE, height=FALSE)


# DIVIDINDO A JANELA____________________________________________________
frame_cima = Frame(janela, width=310, height=50, bg=co3, relief='flat')
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=310, height=250, bg=co3, relief='flat')
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)



# CONFIGURANDO FRAME CIMA________________________________________________
l_nome = Label(frame_cima, text='LOGIN', anchor=NE, font=('Ivy 25'), bg=co3, fg=co2)
l_nome.place(x=5, y=5)


l_linha = Label(frame_cima, text='', width=275, anchor=NW, font=('Ivy 1'), bg=co0, fg=co2)
l_linha.place(x=10, y=45)


# CRIANDO BANCO DE DADOS_________________________________________________
credenciais = ['Anderson Luigui', '123456789']

# CRIANDO FUNÇÃO PARA VERIFICAR LOGIN____________________________________
def verifica_senha():
    nome = e_nome.get()
    senha = e_pass.get()

    if nome =='admin' and senha =='admin':
        messagebox.showinfo('Login', 'Seja bem vindo Admin !')
    elif credenciais[0] == nome and credenciais[1] ==senha:
        messagebox.showinfo('Login', 'Seja bem vindo de volta !' + credenciais[0])

                # DELETAR ITENS PRESENTES NO FRAME
        for widget in frame_baixo.winfo_children():
            widget.destroy()

        for widget in frame_cima.winfo_children():
            widget.destroy()

        nova_janela()

    else:
        messagebox.showwarning('Erro', 'Verifique o nome e senha novamente !')

# CRIANDO FUNÇÃO PARA JANELA APÓS VERIFICAÇÃO________________________________
def nova_janela():
    l_nome = Label(frame_cima, text='Usuário: '+credenciais[0], anchor=NE, font=('Ivy 15'), bg=co3, fg=co2)
    l_nome.place(x=5, y=5)

    l_linha = Label(frame_cima, text='', width=275, anchor=NW, font=('Ivy 1'), bg=co0, fg=co2)
    l_linha.place(x=10, y=45)

    l_nome = Label(frame_baixo, text='Seja bem vindo! '+credenciais[0], anchor=NE, font=('Ivy 15'), bg=co3, fg=co2)
    l_nome.place(x=5, y=105)


# CONFIGURANDO FRAME BAIXO________________________________________________
# CRIANDO LABELS E ENTRY__________________________________________________
l_nome = Label(frame_baixo, text='Nome *', anchor=NW, font=('Ivy 10 bold'), bg=co3, fg=co2)
l_nome.place(x=10, y=20)
e_nome = Entry(frame_baixo, width=25, justify='left', font=("", 15), highlightthickness=1, relief='solid')
e_nome.place(x=14, y=50)


l_pass = Label(frame_baixo, text='Senha *', anchor=NW, font=('Ivy 10 bold'), bg=co3, fg=co2)
l_pass.place(x=10, y=95)
e_pass = Entry(frame_baixo, width=25, justify='left', show='*', font=("", 15), highlightthickness=1, relief='solid')
e_pass.place(x=14, y=130)


# CRIANDO BOTÃO____________________________________________________________________
b_confirmar = Button(frame_baixo, command=verifica_senha, width=39, height=2, text='Entrar', font=('Ivy 8 bold'), bg=co0, fg=co4, relief=RAISED, overrelief=RIDGE)
b_confirmar.place(x=15, y=180)



















janela.mainloop()
