# 17. Crie um programa em Python que solicite ao usuário o valor de uma compra. Aplique
# descontos progressivos de acordo com o valor da compra: 10% para compras até R$ 50,

def descontos_progressivos(valor_compra):
    if valor_compra <= 50:
        desconto = valor_compra - (valor_compra * 0.10)
        return desconto
    elif valor_compra <= 100:
        desconto = valor_compra - (valor_compra * 0.15)
        return desconto
    else:
        desconto = valor_compra - (valor_compra * 0.20)
        return desconto

try:
    valor_compra = float(input('Insira o valor da compra: R$'))
    print(descontos_progressivos(valor_compra))
except ValueError:
    print('ERRO: Insira apenas números!')
