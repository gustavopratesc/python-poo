soma = 0
while True:
    numero = int(input('Insira um numero: '))
    soma += numero
    continuar = input('Quer continuar? [S/N]: ').strip().title()
    if continuar in ['NÃO', 'N', 'NAO']:
        print(f'Soma de todos os números digitados: {soma}')
        break