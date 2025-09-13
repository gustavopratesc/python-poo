# 18. Crie um programa em Python que leia 3 números e imprima o maior e o menor deles.

def maior_menor(lista_numeros):
    maior = max(lista_numeros)
    menor = min(lista_numeros)
    print(f'O maior: {maior} | O menor: {menor}')

lista_numeros = []

try:
    for i in range(3):
        numero = int(input(f'Insira o {i + 1}° numero: '))
        lista_numeros.append(numero)
    maior_menor(lista_numeros)
except ValueError:
    print('ERRO: Insira apenas números!')

