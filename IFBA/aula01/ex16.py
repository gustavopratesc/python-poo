# 16. Crie um programa em Python que solicite ao usuário o raio da base e a altura de uma
# caixa d'água cilíndrica, calcule, e imprima na tela o seu volume em litros. Usar o módulo
# math.
# V = π * r² * h
def volume(raio, altura):
    from math import pi, pow
    v = pi * pow(raio, 2) * altura
    return v * 1000

try:
    raio = float(input('Insira o raio da base: '))
    altura = float(input('Insira a altura: '))
    print(f'O volume é = {volume(raio, altura):.2f}')
except ValueError:
    print('ERRO: Valor inserido não é númerico!')