def produtos(*args):
    resultado = 1
    for n in args:
        resultado *= n
    print(f'O total ficou: R${resultado:.2f}')

lista_precos = []

while True:
    numero = float(input('Insira o preço: R$'))
    lista_precos.append(numero)
    while True:
        continuar = input('Quer continuar? [S/N]: ').strip().upper()
        if continuar in ['SIM', 'S']:
            break
        elif continuar in ['NÃO', 'N']:
            print('respostas...')
            produtos(*lista_precos)
            fim = True
            break
        else:
            print('ERRO: Digite entre [S/N]')
    if 'fim' in locals() and fim:
        break


    #################

## maneiras de parar o loop

fim = False  # começa como falso

while True:
    numero = float(input('Insira o preço: R$'))
    lista_precos.append(numero)

    while True:
        continuar = input('Quer continuar? [S/N]: ').strip().upper()
        if continuar in ['SIM', 'S']:
            break
        elif continuar in ['NÃO', 'NAO', 'N']:
            print('respostas...')
            produtos(*lista_precos)
            fim = True  # ativa a flag
            break
        else:
            print('ERRO: Digite entre [S/N]')

    if fim:  # checa a flag
        break


###############

lista_precos = []
continuar = "S"

while continuar in ["S", "SIM"]:
    numero = float(input('Insira o preço: R$'))
    lista_precos.append(numero)

    continuar = input('Quer continuar? [S/N]: ').strip().upper()

print('respostas...')
produtos(*lista_precos)
