# 8. Crie um programa em Python que leia um número e imprima o seu valor absoluto,
# independente dele ser positivo ou negativo, sem uso de biblioteca matemática.

def valor_absoluto(numero):
    if numero < 0:
        numero_absoluto = -numero
        return numero_absoluto
    return numero

try:
    numero = int(input('Insira o número: '))
    print(f'O valor absoluto desse número é {valor_absoluto(numero)}')
except ValueError:
    print('ERRO: Insira apenas números!')