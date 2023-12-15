import tkinter as tk

def substituir_letras():
    texto_original = entrada_texto.get()
    letra_substituir = entrada_letra_substituir.get()
    letra_substituta = entrada_letra_substituta.get()

    texto_modificado = texto_original.replace(letra_substituir, letra_substituta)
    
    resultado.config(text="Texto modificado: " + texto_modificado)

# Criar a janela principal
janela = tk.Tk()
janela.title("Substituidor de Letras")

# Criar entrada de texto
rotulo_texto = tk.Label(janela, text="Digite o texto:")
rotulo_texto.pack(pady=5)
entrada_texto = tk.Entry(janela, width=40)
entrada_texto.pack(pady=5)

# Criar entrada para a letra a ser substituída
rotulo_letra_substituir = tk.Label(janela, text="Letra a ser substituída:")
rotulo_letra_substituir.pack(pady=5)
entrada_letra_substituir = tk.Entry(janela, width=5)
entrada_letra_substituir.pack(pady=5)

# Criar entrada para a letra substituta
rotulo_letra_substituta = tk.Label(janela, text="Letra substituta:")
rotulo_letra_substituta.pack(pady=5)
entrada_letra_substituta = tk.Entry(janela, width=5)
entrada_letra_substituta.pack(pady=5)

# Criar botão para substituir letras
botao_substituir = tk.Button(janela, text="Substituir Letras", command=substituir_letras)
botao_substituir.pack(pady=10)

# Exibir resultado
resultado = tk.Label(janela, text="Texto modificado: ")
resultado.pack()

# Iniciar loop da interface gráfica
janela.mainloop()


