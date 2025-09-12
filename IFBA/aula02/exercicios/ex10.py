# 10. Crie um programa em Python que leia um número e imprima se ele é positivo, negativo
# ou neutro

def classificacao(numero):
    if numero > 0:
        print(f'Esse número é positivo: {numero}')
    elif numero == 0:
        print(f'Esse número é neutro o 0')
    else:
        print(f'Esse número e negativo: {numero}')


try:
    numero = int(input('Insira um número: '))
    classificacao(numero)
except ValueError:
    print('ERRO: Insira apenas números!')