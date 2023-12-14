import tkinter as tk
from tkinter import messagebox

def calcular_fatorial():
    try:
        numero = int(entrada_numero.get())
        resultado = 1

        if numero < 0:
            messagebox.showerror("Erro", "Por favor, insira um número não negativo.")
        else:
            for i in range(1, numero + 1):
                resultado *= i

            messagebox.showinfo("Resultado", f"O fatorial de {numero} é {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número inteiro.")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Calculadora de Fatorial")

# Rótulo
label_instrucao = tk.Label(root, text="Digite um número para calcular o fatorial:")
label_instrucao.pack(pady=10)

# Entrada de texto
entrada_numero = tk.Entry(root)
entrada_numero.pack(pady=10)

# Botão de cálculo
botao_calcular = tk.Button(root, text="Calcular Fatorial", command=calcular_fatorial)
botao_calcular.pack(pady=10)


root.mainloop()
