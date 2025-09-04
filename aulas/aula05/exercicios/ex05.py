def filtar(*args):
    pares = [n for n in args if n % 2 == 0]
    return pares
        


fim = False

lista_numeros = []

while True:
    numero = int(input('Insira um número: '))
    lista_numeros.append(numero)

    while True:
        continuar = input('Quer continuar? [S/N]: ').strip().upper()
        if continuar in ['S', 'SIM']:
            break
        elif continuar in ['N', 'NÃO', 'NAO']:
            print('respostas...')
            print(f'Números pares: {filtar(*lista_numeros)}')
            fim = True
            break
        else:
            print(f'ERRO: Você digitou {continuar} digite apenas [S/N]!')

    if fim:
        break