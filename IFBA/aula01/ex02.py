'''2. Crie um programa em Python que leia 2 valores e escreva na tela a média ponderada
entre eles. O primeiro valor tem peso 40%, e o segundo valor tem peso 60%.'''

def media_ponderada(valor1, valor2):
    media = ((valor1 * 40) + (valor2 * 60)) / 100
    return media


try:
    valor1 = float(input('Insira um valor: '))
    valor2 = float(input('Insira outro valor: '))
    print(f'A media ponderada dos dois valores é {media_ponderada(valor1, valor2)}')
except ValueError:
    print('ERRO: Erro insira um número!')