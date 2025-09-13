# 26. Crie um programa em Python que peça ao usuário as coordenadas (x, y) de um ponto.
# Imprima em qual quadrante do plano cartesiano esse ponto se encontra.

def plano_cartesiano(x, y):
    if x > 0 and y > 0:
        print(f'Se encontra no primeiro quadrante ({x}, {y})')
    elif x < 0 and y > 0:
        print(f'Se encontra no segundo quadrante ({x}, {y})')
    elif x < 0 and y < 0:
        print(f'Se encontra no terceiro quadrante ({x}, {y})')
    else:
        print(f'Se encontra no quarto quadrante ({x}, {y})')

try:
    x = float(input('Insira a coordenada X: '))
    y = float(input('Insira a coordenada Y: '))
    plano_cartesiano(x, y)
except ValueError:
    print('ERRO: Insira apenas números!')