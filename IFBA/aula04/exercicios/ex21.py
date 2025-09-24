# 22. Conte e imprima quantas vogais há numa lista de caracteres


lista_caracters = ['a', 'b', 'c', 'd', 'e', 'u', 'o', 'i']

contador = 0

for i in lista_caracters:
    if i in 'aeiouAEIOU':
        contador += 1

print(contador)