# 29. Crie um programa em Python que leia 3 números referentes a 3 tamanhos e indique se
# eles formam ou não formam um triângulo.

def triangulo(n1, n2, n3):
    if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
        print('Sim forma um triangulo')
    else:
        print('Não forma')

try:
    n1 = int(input('Insira o primeiro número: '))
    n2 = int(input('Insira o segundo número: '))
    n3 = int(input('Insira o terceiro número: '))
    triangulo(n1, n2, n3)
except ValueError:
    print('ERRO: Insira apenas números!')
