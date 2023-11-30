import tkinter as tk

def mostrar_mensagem():
    label.config(text="Olá, Puta!")

# criar uma janela
janela = tk.Tk()
janela.title("Exemplo de GUI em Python")

#Criar um rótulo 
label = tk.Label(janela, text="Bem vindo á interface grafica de usuario")
label.pack(padx=10, pady=10)

# Criar um botão do tipo CTA (Call to action)
botao = tk.Button(janela,text="clique aqui!", command=mostrar_mensagem)
botao.pack(padx=10, pady=10)


# Iniciar a GUI em loop
janela.mainloop()