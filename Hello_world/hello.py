import tkinter as tk
from tkinter import messagebox as mb

# Criar o Frame principal
janela = tk.Tk()
janela.geometry('400x200')
janela.title('Inverter Frase')
janela.resizable(False, False)

def inverter_frase():
    try:
        frase = campo_frase.get()
        if not frase:
            mb.showwarning(title='Aviso', message='Digite uma frase antes de inverter.')
            return
        
        lista_caracteres = list(frase)
        lista_caracteres.reverse()
        frase_invertida = ''.join(lista_caracteres)
        mb.showinfo(title='Resultado', message=f'Frase Invertida: {frase_invertida}')
    except Exception as e:
        mb.showerror(title='Erro', message=f'Ocorreu um erro: {str(e)}')

def limpar():
    campo_frase.delete(0, tk.END)

# Criar Label e Campo para a frase
label_frase = tk.Label(text='Frase:', height=2, font=('Impact', 14, 'italic'))
label_frase.grid(column=0, row=0)

campo_frase = tk.Entry(width=30, font=('Impact', 14))
campo_frase.grid(column=1, row=0)

# Botão para inverter a frase
botao_inverter = tk.Button(text='Inverter', command=inverter_frase, font=('Impact', 14))
botao_inverter.grid(column=0, row=1, padx=10, pady=10)

# Botão para limpar o campo de entrada
botao_limpar = tk.Button(text='Limpar', command=limpar, font=('Impact', 14))
botao_limpar.grid(column=1, row=1, padx=10, pady=10)

# Começar a GUI
janela.mainloop()
