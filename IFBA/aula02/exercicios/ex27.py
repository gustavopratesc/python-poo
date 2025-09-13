# 27. Crie um programa em Python que leia 3 números e informe se a mediana é maior,
# menor ou igual à média aritmética dos números informados.

lista_numeros = []

for i in range(3):
    numero = int(input(f'Insira o {1 + i}° numero: '))
    lista_numeros.append(numero)



media_numeros = sum(lista_numeros) / len(lista_numeros)
numeros_ordenados = sorted(lista_numeros)


print(numeros_ordenados)
print(f'{media_numeros:.2f}')

if numeros_ordenados[1] > media_numeros:
    print('É maior')
else:
    print('É menor')