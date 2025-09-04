def soma(*args):
    total = sum(args)
    print(f'A soma de todos os números é: {total}')


numeros = []

while True:
    print('Digite números para somar ou 0 para finalizar: ')
    print('-' * 20)
    numero = int(input('Número: '))
    if numero == 0:
        soma(*numeros)
        break

    numeros.append(numero)