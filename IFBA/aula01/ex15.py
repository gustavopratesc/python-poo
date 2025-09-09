# 15. Crie um programa em Python que solicite ao usuário o raio e calcule e imprima o
# perímetro e a área do círculo correspondente. Usar o módulo math

import math

def perimetro_e_area(raio):
    perimetro = 2 * math.pi * raio
    area = math.pi * math.pow(raio, 2)
    print(f'O perimetro do circulo é {perimetro:.2f}')
    print(f'A area do circulo é {area:.2f}')

try:
    raio = float(input('Insira o raio: '))
    perimetro_e_area(raio)
except ValueError:
    print('ERRO: Digite apenas números!')