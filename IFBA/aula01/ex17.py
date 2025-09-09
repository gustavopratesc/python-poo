# 17. Crie um programa em Python que solicite ao usuário o valor do raio de uma esfera e
# calcule e imprima o volume dessa esfera. Usar o módulo math.

def volume_esfera(raio):
    import math
    volume = (4/3) * math.pi * math.pow(raio, 3)
    print(f'O volume da esfera é: {volume:.2f}')

try:
    raio_esfera = float(input('Insira o raio da esfera: '))
    volume_esfera(raio_esfera)
except ValueError:
    print('ERRO: Insira apenas números!')