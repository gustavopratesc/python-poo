'''4. Crie um programa em Python que imprima a tabuada de multiplicação de um número
fornecido pelo usuário.
'''


def tabuada(numero):
    print(f'A tabuada do número {numero} é: ')
    for i in range(11):
        print(f'{numero} x {i} = {numero * i}')

try:
    numero = int(input('Insira o número para tabuada: '))
    tabuada(numero)
except ValueError:
    print('ERRO: Insira apenas números!')

##

def tabuada_while(numero):
    contador = 0
    print(f'A tabuada de {numero} é: ')
    while contador <= 10:
        print(f'{numero} x {contador} = {numero * contador}')
        contador += 1

try:
    n = int(input('Insira o número para tabuada!: '))
    tabuada_while(n)
except ValueError:
    print('ERRO: Insira apenas números!')

