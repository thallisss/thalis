# ERP app

import tkinter as tk 
from tkinter import messagebox
import pesquisar_produto as pp 


def abrir_janela(mensagem):
    nova_janela = tk.Toplevel()
    nova_janela.title("Ação qualquer...")

    label = tk.Label(nova_janela, text=mensagem, padx=20,pady=20)
    label.pack()

    botao_fechar = tk.Button(nova_janela, text="SAIR", command=nova_janela.destroy)
    botao_fechar.pack(padx=20, pady=10)

# funções para as diferentes funcionalidades do sistema ERP

def pesquisar_produto():
    abrir_janela("Pesquisar produto")

def checar_estoque():
    abrir_janela("Checar estoque")

def acrescentar_estoque():
    abrir_janela("Acrescentar estoque")

def remover_estoque():
    abrir_janela("Remover estoque")

def cadastrar_produto():
    abrir_janela("Cadastrar produto")

#Criar janela principal

janela_principal = tk.Tk()
janela_principal.title("SISTEMA ERP PUTA!")
janela_principal.attributes('-fullscreen', True)

#configurar icons de menu

icon_pesquisar = tk.PhotoImage(file="lupa.png")
icon_estoque = tk.PhotoImage(file="box.png")
icon_acrescentar = tk.PhotoImage(file="add.png")
icon_remover = tk.PhotoImage(file="lixo.png")
icon_cadastrar = tk.PhotoImage(file="bla.png")

# Criar botões dos icones
botao_pesquisar = tk.Button(janela_principal, image=icon_pesquisar, command=pesquisar_produto)
botao_estoque = tk.Button(janela_principal, image=icon_estoque, command=checar_estoque )
botao_acrescentar = tk.Button(janela_principal, image=icon_acrescentar, command=acrescentar_estoque)
botao_remover = tk.Button(janela_principal, image=icon_remover, command=remover_estoque)
botao_cadastrar = tk.Button(janela_principal, image=icon_cadastrar, command=cadastrar_produto)

# exibir botões na janela 

botao_pesquisar.pack()
botao_estoque.pack()
botao_acrescentar.pack()
botao_remover.pack()
botao_cadastrar.pack()

# loop da janela principal 
janela_principal.mainloop()
