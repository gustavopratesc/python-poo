# 1. Crie um programa em Python que leia dois valores numéricos, e calcule e exiba na tela a
# média aritmética deles.

def media(n1, n2):
    media_valor = (n1 + n2) / 2
    return media_valor


try:
    n1 = float(input('Insira a nota: '))
    n2 = float(input('Insira a outra nota: '))
    print(f'A media dos dois números é: {media(n1, n2):.2f}')
except ValueError:
    print('ERRO: Insira apenas números!')