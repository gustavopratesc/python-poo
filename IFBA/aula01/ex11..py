# Crie um programa em Python que solicite ao usuário dois números inteiros e, em
# seguida, imprima o resultado da potenciação do primeiro pelo segundo. Usar o módulo
# math

from math import pow

def potencia(n1, n2):
    potencia = pow(n1, n2)
    print(f'A potencia entre {n1} elevado a {n2} é igual a: {potencia}')

try:
    n1 = int(input('Insira um número: '))
    n2 = int(input('Insira o segundo número: '))
    potencia(n1, n2)
except ValueError:
    print(f'ERRO: insira apenas números inteiros!')