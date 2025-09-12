# 13. Crie um programa em Python que peça ao usuário o valor de um produto e, se esse
# valor for maior que R$ 100,00, aplique um desconto de 5%.

def desconto(valor):
    if valor > 100:
        print(f'Você recebeu 5% de desconto')
        desconto = valor - (valor * 0.05)
        print(f'O valor antigo R${valor} o Valor com desconto R${desconto:.2f}')
        return
    
    print(f'Seu produto deu R${valor} ! Você quer pagar em dinheiro, cartão, etc...')

try:
    valor_produto = float(input('Insira o valor do produto: R$'))
    desconto(valor_produto)
except ValueError:
    print('ERRO: Insira apenas números!')