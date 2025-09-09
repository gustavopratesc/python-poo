# Crie um programa em Python que leia um ângulo em graus, calcule e imprima o seno e o
# cosseno dele. Usar o módulo math.

from math import sin, cos, radians

def seno_cosseno(angulo):
    radiano = radians(angulo)
    cosseno = cos(radiano)
    seno = sin(radiano)
    print(f'Angulo {angulo}° | Radiano {radiano:.2f}° | Cosseno {cosseno:.2f}° | Seno {seno:.2f}')


try:
    angulo = float(input('Insira o angulo: °'))
    seno_cosseno(angulo)
except ValueError:
    print('ERRO: Valor inserido não é númerico!')