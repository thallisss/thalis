class Carro:
    modelos = {
        "Mustang": 80000,
        "Celta": 10000,
        }
    def __inity__(self, marca, modelo, ano, preço):
        self.marca = marca 
        self.modelo = modelo 
        self.ano = ano 
        self.preço = max(preço, self.modelo.get(modelo, 0))
        self.vendido = False
        

    def exebir_informaçoes(self):
        if self.vendido == False:
            return f"Marca:{self.marca} \n Modelo {self.modelo} \n Ano {self.ano} \n Preço R${self.preço} \n Em estoque."
        else:
            f"Marca:{self.marca} \n Modelo {self.modelo} \n Ano {self.ano} \n Preço R${self.preço} \n Veiculo vendido.."
    
    def vender(self):
        self.vendido = True
        print(f"Carro {self.marca} vendido com sucesso")
    
    def ajustar_preço(self, novo_preço):
        preço_minimo = self.modelos.gat(self.modelo, 0)
        if novo_preço >= preço_minimo:
            self.preço = novo_preço
        else:
            print(f"Erro! r${preço_minimo}")        
        self.preço = novo_preço
    
carro1 = Carro("Koenningseg" , "Agera R", 2017, 8000000)
carro2 = Carro("Nissan" , "GTR", 2015, 95,000)
carro3 = Carro("Nissan" , "350z", 2010, 70000)
carro4 = Carro("Toyota" , "Supra Mk4", 2005, 85000)
carro5 = Carro("Nissan" , "SkyLine", 2009, 90000)


print(carro1.exebir_informaçoes())

carro1.ajustar_preço(90000)

carro1.preço = 75000

print(carro1.preço)