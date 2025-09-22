# 15. Crie um programa em Python que leia um valor de "b" e um valor de "n", calcule e
# escreve a valor de b elevado a n (sem uso de função matemática). Ex: b = 5, n = 3, b*b*b =
# 125.

def potencia(base, expoente):
    resultado = 1
    for _ in range(expoente):
        resultado *= base
    
    print(resultado)

try:
    base = int(input('Insira o número da base: '))
    expoente = int(input('Insira o número do expoente: '))
    potencia(base, expoente)
except ValueError:
    print('ERRO: Insira apenas números!')