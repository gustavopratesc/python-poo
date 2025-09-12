from functools import reduce

numeros = [5, 8, 10, 20]


soma = reduce(lambda acc, x: acc + x, numeros)

print(soma)