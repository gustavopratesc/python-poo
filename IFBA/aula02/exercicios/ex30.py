# 30. Crie um programa em Python que leia 3 números referentes a 3 lados de um
# triângulo e indique se eles formam um triângulo equilátero, escaleno ou isósceles.

def triangulo(lado1, lado2, lado3):
    if not (lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1):
        print('Os lados informados não formam um triângulo')
        return


    if lado1 == lado2 == lado3:
        print('É equilatero')
        return
    if lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print('É escaleno')
        return
    else:
        print('É isósceles')

try:
    lado1 = int(input('Insira o primeiro lado: '))
    lado2 = int(input('Insira o segundo lado: '))
    lado3 = int(input('Insira o terceiro lado: '))
    triangulo(lado1, lado2, lado3)
except ValueError:
    print('ERRO: Insira apenas números inteiros!')