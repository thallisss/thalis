def contar_letra(letra):
    texto = input("digite uma palavra:  ").lower()
    return texto.count(letra)


letra_a_contar = "a"
print("a palavra contem", contar_letra(letra_a_contar), letra_a_contar)
