# 22. Crie um programa em Python que gere um número aleatório entre 1 e 10 e peça ao
# usuário para adivinhar. Imprima se ele acertou ou errou

from random import randint

numeros_aleatorios = randint(1, 10)

while True:
    try:
        numero = int(input('Insira um número entre 1 a 10: '))
        if numero == numeros_aleatorios:
            print('Você acertou!')
            print(f'Número sorteado {numeros_aleatorios}')
            break
        else:
            print('Você errou!')
            continue
    except ValueError:
        print('ERRO: Insira apenas números!')

