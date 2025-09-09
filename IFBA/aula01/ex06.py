# 6. Crie um programa em Python que peça ao usuário para inserir dois números inteiros e,
# em seguida, imprima o resultado da divisão do primeiro pelo segundo, considerando
# somente a parte inteira.

def divisao_inteira(valor1, valor2):
    div = valor1 // valor2
    print(f'A divisão inteira entre o 1° {valor1} pelo 2° {valor2} é: {div}')


try:
    valor1 = float(input('Insira o 1° valor: '))
    valor2 = float(input('Insira o 2° valor: '))
    divisao_inteira(valor1, valor2)
except ValueError:
    print('ERRO: Digite apenas números!')