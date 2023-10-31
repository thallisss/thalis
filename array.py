import array as arr
my_array = arr.array('i')
for i in range(5):
    num = int(input("insira um numero: "))
    my_array.append(num)
print("Array resultante: ", my_array)
print(sum(my_array))
min_valor = min(my_array)
max_valor = max(my_array)
print(f"O menor valor e : {min_valor}\nO maior valor e {max_valor}")
my_array.pop()
print("Removido o último elemento", my_array)
my_array.reverse()
print("Lista invertida: ", my_array)