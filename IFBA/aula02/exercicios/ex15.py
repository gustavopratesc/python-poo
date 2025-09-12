# 15. Crie um programa em Python que leia o preço de um produto e escreva o valor de
# venda final dele. O vendedor quer vendê-lo com 40% de lucro se o valor da compra for
# menor que R$20,00; caso contrário, o lucro será de 30%

def lucro(preco):
    if preco < 20:
        novo_lucro = preco - (preco * 0.04)
        return f'Você teve um lucro de R${novo_lucro:.2f} | 40%'
    else:
        novo_lucro = preco - (preco * 0.03)
        return f'Você teve um lucro de R${novo_lucro:.2f} | 30%'



try:
    preco_produto = float(input('Insira o preço do produto: '))
except ValueError:
    print('ERRO: Insira apenas números!')