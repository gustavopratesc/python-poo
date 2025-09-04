def multiplica(*args):
    resultado = 1
    for n in args:
        resultado *= n
    print(f'O total ficou: {resultado:.2f}')


lista_numeros = []

continuar = 'S'

while continuar in ['SIM', 'S']:
    numero = int(input('Insira um número: '))
    lista_numeros.append(numero)

    continuar = input('Quer continuar? [S/N]: ').strip().upper()


print('Respostas...')
multiplica(*lista_numeros)