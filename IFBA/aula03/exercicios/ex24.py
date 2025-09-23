# 26. Crie um programa em Python que solicite ao usuário um número e imprima os seus
# divisores.

def divisores(numero):
    for i in range(1, numero + 1):
        if numero % i == 0:
            print(i)

try:
    numero = int(input('Insira seu número: '))
    divisores(numero)
except ValueError:
    print('ERRO: Insira apenas números!')