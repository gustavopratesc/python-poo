# 27. Crie um programa em Python que peça ao usuário um número e imprima se é primo ou
# não.

def numero_primo(numero):
    if numero <= 1:
        print('Não é primo!')
    else:
        print('É primo')

try:
    numero = int(input('Insira um número: '))
except ValueError:
    print('ERRO: Insira apenas números!')