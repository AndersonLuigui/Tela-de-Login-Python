from tkinter import *
from tkinter import Tk, ttk

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

janela.mainloop()
