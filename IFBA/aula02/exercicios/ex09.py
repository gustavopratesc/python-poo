# 9. Crie um programa em Python que leia um número inteiro e escreva se ele é par ou ímpar

def par_ou_impar(numero):
    if numero % 2 == 0:
        print(f'O número {numero} é par!')
    else:
        print(f'O número {numero} é impar')

try:
    numero = int(input('Insira um número: '))
    par_ou_impar(numero)
except ValueError:
    print('ERRO: Insira apenas números!')