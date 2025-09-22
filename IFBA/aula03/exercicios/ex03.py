# 3. Crie um programa em Python que peça ao usuário um número e imprima os números de
# 1 até esse número.

try:
    numero = int(input('Insira um número: '))
    for i in range(0, numero):
        print(i + 1)
except ValueError:
    print('ERRO: Insira apenas números inteiros!')


contador = 1

try:
    n = int(input('Insira o número: '))
    while contador <= n:
        print(contador)
        contador += 1
except ValueError:
    print('ERRO: Insira apenas números!')