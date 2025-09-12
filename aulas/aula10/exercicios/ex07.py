numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

numeros_pares = filter(lambda numero: numero % 2 == 0, numeros)
numeros_pares = list(numeros_pares)

print(numeros_pares)
# filter para filtrar, map para mudar, sorted para ordenar
numeros_dobrados_pares = map(lambda numero: numero * 2, numeros_pares)

print(list(numeros_dobrados_pares))