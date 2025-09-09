# 14. Crie um programa em Python que peça ao usuário para inserir um número decimal e,
# em seguida, calcule e imprima a parte fracionária desse número.

def parte_fracionaria(number):
    fracionaria = number % 1
    return fracionaria

try:
    number = float(input('Insira um número decimal: '))
    print(f'A parte fracionaria do número {number} é: {parte_fracionaria(number)}')
except ValueError:
    print('ERRO: Insira apenas números!')