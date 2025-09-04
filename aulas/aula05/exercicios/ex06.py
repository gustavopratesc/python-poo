# Caixa registradora com desconto 🛒
# Crie uma função caixa(*args) que recebe preços de produtos e retorna o total da compra.

# Se o total for maior que 100, aplique um desconto de 10%.

def caixa(*args):
    total = sum(args)
    if total > 100:
        desconto = total - (total * 0.10)
        print(f'Compra total: R${total:.2f} | Você recebeu 10% desconto R${desconto:.2f}')
    else:
        print(f'Sua compra ficou R${total:.2f}')

lista_precos = []

continuar = 'S'

while continuar in ['SIM', 'S']:
    numero = int(input('Digite o preço: R$'))
    lista_precos.append(numero)

    continuar = input('Quer continuar? [S/N]: ').strip().upper()

print('Respostas...')
caixa(*lista_precos)