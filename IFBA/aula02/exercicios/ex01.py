# 1. Crie um programa em Python que peça ao usuário um número de 1 a 7 e imprima o dia
# da semana correspondente

def dia_semana(dia):
    if dia == 1:
        print('Hoje é segunda-feira')
    elif dia == 2:
        print('Hoje é terça-feira')
    elif dia == 3:
        print('Hoje é quarta-feira')
    elif dia == 4:
        print('Hoje é quinta-feira')
    elif dia == 5:
        print('Hoje é sexta-feira')
    elif dia == 6:
        print('Hoje é sabado')
    elif dia == 7:
        print('Hoje é domingo')
    else:
        print('Digite entre 1 a 7 para saber o dia da semana!')

try:
    numero = int(input('Insira um número de 1 a 7: '))
    dia_semana(numero)
except ValueError:
    print('ERRO! Insira apenas números!')