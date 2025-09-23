# 7. Em uma lista de números, calcule a soma dos elementos que estão em posições pares
# (índices pares, considerando índice começando em 0).

lista_numeros = [5, 1, 5, 1, 5]
soma = 0
for i, n in enumerate(lista_numeros):
    if i % 2 == 0:
        soma += n


print(soma)