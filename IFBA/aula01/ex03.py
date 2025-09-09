# 3. Crie um programa em Python que leia 3 valores e escreva na tela a média ponderada
# entre eles. O primeiro valor tem peso 4, o segundo valor tem peso 7 e o terceiro valor tem
# peso 3.

def media_ponderada(valor1, valor2, valor3):
    media = ((valor1 * 4) + (valor2 * 7) + (valor3 * 3)) / (4 + 7 + 3)
    print(f'A media ponderada dos 3 valores é {media:.2f}')


try:
    valor1 = float(input('Insira o 1° valor: '))
    valor2 = float(input('Insira o 2° valor: '))
    valor3 = float(input('Insira o 3° valor: '))
    media_ponderada(valor1, valor2, valor3)
except ValueError:
    print('ERRO: Digite apenas números!')