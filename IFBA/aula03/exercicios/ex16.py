# 16. Crie um programa em Python que leia um número e devolva o fatorial dele.

def fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    print(resultado)

try:
    numero = int(input('Insira o número para o fatorial: '))
    fatorial(numero)
except ValueError:
    print('ERRO: Insira apenas números!')