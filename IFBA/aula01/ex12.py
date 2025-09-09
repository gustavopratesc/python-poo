# Crie um programa em Python que declare uma variável do tipo ponto flutuante e atribua
# a ela um valor. Em seguida, calcule e imprima a raiz quadrada desse valor. Usar o módulo
# math.

from math import sqrt

def raiz(numero):
    numero_raiz = sqrt(numero)
    return numero_raiz

try:
    numero = float(input('Insira um número: '))
    print(f'A raiz do número {numero} é: {raiz(numero):.2f}')
except ValueError:
    print('ERRO: Digite apenas números!')