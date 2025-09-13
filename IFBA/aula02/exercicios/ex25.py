# 25. Crie um programa em Python que leia 2 números e uma operação aritmética (+,-,*,/),
# calcule e escreva o resultado dessa operação aplicada aos números.

def mini_calculadora(n1, n2, operacao):
    if operacao == '+':
        return n1 + n2
    elif operacao == '-':
        return n1 - n2
    elif operacao == '*':
        return n1 * n2
    elif operacao == '/':
        return n1 / n2
    else:
        print('Digite os operadores corretos! (+ - * /)')

try:
    n1 = int(input('Insira um número: '))
    n2 = int(input('Insira outro número: '))
    operacao = input('Insira uma operacao (+ - * /): ')
    print(f'O resultado da operação ficou: {mini_calculadora(n1, n2, operacao)}')
except ValueError:
    print('ERRO: Insira apenas números!')
    