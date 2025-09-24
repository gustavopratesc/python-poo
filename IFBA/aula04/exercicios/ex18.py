# 18. Dadas duas listas do mesmo tamanho, multiplique elemento a elemento e guarde os
# resultados em uma terceira lista.

lista_1 = [1, 3, 7, 10, 15]
lista_2 = [5, 7, 12, 6, 10]

lista_3 = []

for i in range(len(lista_1)):
    produto = lista_1[i] * lista_2[i]
    lista_3.append(produto)

print(lista_3)

## ou usando list crompression

lista_3 = [x * y for x, y in zip(lista_1, lista_2)]