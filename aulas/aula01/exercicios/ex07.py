def tabuada(numero):
    print(f'A tabuada desse número {numero} é:')
    for i in range(1, 11):
        print(f'{numero} x {i} = {numero * i}')

try:
    numero = int(input('Insira um número para tabuada: '))
    tabuada(numero)
except ValueError:
    print('ERRO: Valor digitado não é númerico!')