# 21. Crie um programa em Python que solicite três números ao usuário e imprima quantos
# deles são positivos

contador = 0

try:
    n1 = float(input('Insira o 1° número: '))
    n2 = float(input('Insira o 2° número: '))
    n3 = float(input('Insira o 3° número: '))
except ValueError:
    print('ERRO: Insira apenas números!')

if n1 > 0:
    contador += 1

if n2 > 0:
    contador += 1

if n3 > 0:
    contador += 1

print(f'Números positivos: {contador}')