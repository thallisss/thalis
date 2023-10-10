
"""

class MinhaClasse:
    nome = "thallis"

p1 = MinhaClasse()
print(p1.nome)

"""
"""
class Pessoa:
    def __init__(self, nome, idade ):
        self.nome = nome
        self.idade = idade
        self.habilitaçao = habilitaçao

    def __str__(self):
        return f" O seu nome é {self.nome} e sua idade é{self.idade}!"
    
    def maioridade(self):
        if self.idade > 17:
            print(f"Voce e maior de idade, tem é{self.idade} anos nas costas")
        else:
            print("Voce e menor de idade")
    
    def checagem_hab(self):
        return self.habilitaçao
        


usuario1 = Pessoa("Pedro", 97, True)
usuario2 = Pessoa("Maria", 33, False)
print(usuario2.habilitaçao)
usuario2.habilitaçao = True
print()


"""



