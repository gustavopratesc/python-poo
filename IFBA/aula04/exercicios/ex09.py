# 9. Conte quantos elementos pares existem em uma lista de números

lista_numeros = [1, 4, 6, 100]
contador = 0

for n in lista_numeros:
    if n % 2 == 0:
        contador += 1

print(contador)