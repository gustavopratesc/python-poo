# 20. Crie um programa em Python que leia a altura, a base maior e a base menor referentes
# a um trapézio, calcule e mostre na tela a sua área

def area_trapezio(altura, base_maior, base_menor):
    area = (base_maior + base_menor) * (altura / 2)
    print(f'A area do trapezio é: {area:.2f}')

try:
    altura = float(input('Insira a altura do trapézio: '))
    base_maior = float(input('Insira a base maior do trapézio: '))
    base_menor = float(input('Insira a base menor do trapézio: '))
    area_trapezio(altura, base_maior, base_menor)
except ValueError:
    print('ERRO: Digite apenas números!')