# Crie um programa em Python que peça ao usuário para inserir dois números inteiros e,
# em seguida, imprima o resultado arredondado da divisão do primeiro pelo segundo. Usar o
# módulo math

import math

def divisao_arredondada(n1, n2):
    div = n1 / n2
    print(f'A divisão entre {n1} e {n2} é: {math.ceil(div)}')

try:
    n1 = int(input('Insira um número: '))
    n2 = int(input('Insira outro número: '))
    divisao_arredondada(n1, n2)
except ValueError:
    print('ERRO: Insira apenas números interios')