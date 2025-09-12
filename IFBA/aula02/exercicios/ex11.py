# 11. Crie um programa em Python que solicite três números ao usuário e imprima se eles
# estão em ordem crescente, em ordem decrescente ou fora de ordem.

def ordenacao(numero1, numero2, numero3):
    if numero1 < numero2 and numero2 < numero3:
        print('Estão na ordem crescente')
    elif numero1 > numero2 and numero2 > numero3:
        print('Estão na ordem decrescente')
    else:
        print('Estão fora de ordem')
        

try:
    numero1 = int(input('Insira o 1° número: '))
    numero2 = int(input('Insira o 2° número: '))
    numero3 = int(input('Insira o 3° número: '))
    ordenacao(numero1, numero2, numero3)
except ValueError:
    print('ERRO: Insira apenas números!')
    