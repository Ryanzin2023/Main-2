import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *


Frame = tk.Tk()
Frame.geometry('350x300')
Frame.resizable(False, False)
Frame.title('Exemplo Radio Button')
#Frame.tk.call('wd', 'iconphoto', Frame.__w,tk.PhotoImage(file= 'Testes/Python-logo-notext.svg.png'))#



def mostrarEscolha():
    showinfo(title = 'Resultado', message = f'Você escolheu {tam_selecionado.get()}')

lbPergunta = ttk.Label(text= 'Escolha o tamanho:') 
lbPergunta.pack(fill= 'x', padx='15', pady='10')

tam_selecionado = tk.StringVar(Frame, value = 'M')

tamanhos = (('Pequeno', 'P'),
            ('Médio', 'M'),
            ('Grande', 'G'),
            ('Extra Grande', 'XG'),
            ('Extra Extra Grande', 'XXG'))

for tamanho in tamanhos:
    rd= ttk.Radiobutton(Frame, text = tamanho[0],
                    value= tamanho[1],
                    variable= tam_selecionado)
    rd.pack(fill = 'x', padx = 5, pady= 5) #Padding

btEscolha = ttk.Button(Frame, text = 'Ler tamanho', command = mostrarEscolha)
btEscolha.pack(fill = 'x', padx = 15, pady= 5)

Frame.mainloop()