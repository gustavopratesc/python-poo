# 3. Crie um programa em Python que solicite ao usuário um número de 1 a 7 representando
# um dia da semana. Imprima se é um dia útil ou final de semana

def dia_util(dia_semana):
    if 1 < dia_semana <= 5:
        print('Dia util')
    elif 5 < dia_semana <= 7:
        print('Final de semana')
    else:
        print('Digite entre 1 a 7')

try: 
    dia_semana = int(input('Insira um dia da semana 1 a 7: '))
    dia_util(dia_semana)
except ValueError:
    print('ERRO: Insira apenas números inteiros')