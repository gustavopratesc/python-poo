# 19. Crie um programa em Python que leia os catetos de um triângulo retângulo, calcule e
# escreva a hipotenusa correspondente. Usar o módulo math.

import math

def hipotenusa(cateto1, cateto2):
    hipotenusa = math.hypot(cateto1, cateto2)
    return hipotenusa


try:
    cateto1 = float(input('Insira o 1° cateto: '))
    cateto2 = float(input('Insira o 2° cateto: '))
    print(f'A hipotenusa é: {hipotenusa(cateto1, cateto2):.2f}°')
except ValueError:
    print('ERRO: Insira apenas números!')