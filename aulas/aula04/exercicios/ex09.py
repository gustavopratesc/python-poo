def caixa(precos):
    return sum(precos)

lista_precos = []

while True:
    print(f'Digite um preço ou enter para finalizar!')
    preco = input('R$ ')

    if not preco:
        print(f'Preço total: R${caixa(lista_precos):.2f}')
        break

    try:
        preco_modificado = float(preco)
        lista_precos.append(preco_modificado)
    except ValueError:
        print('ERRO: Valor inserido não é númerico')
        continue
