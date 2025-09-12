# 2. Crie um programa em Python que peça ao usuário um número de 1 a 12 e imprima o mês
# correspondente.

def meses_ano(numero_mes):
    if numero_mes == 1:
        print('Janeiro')
    elif numero_mes == 2:
        print('Fevereiro')
    elif numero_mes == 3:
        print('Março')
    elif numero_mes == 4:
        print('Abril')
    elif numero_mes == 5:
        print('Maio')
    elif numero_mes == 6:
        print('Junho')
    elif numero_mes == 7:
        print('Julho')
    elif numero_mes == 8:
        print('Agosto')
    elif numero_mes == 9:
        print('Setembro')
    elif numero_mes == 10:
        print('Outubro')
    elif numero_mes == 11:
        print('Novembro')
    elif numero_mes == 12:
        print('Dezembro')
    else:
        print('Insira entre 1 a 12')

try:
    numero_mes = int(input('Insira algum número referenciando o mês: '))
    meses_ano(numero_mes)
except ValueError:
    print('ERRO: Digite um número inteiro!')

from datetime import date

data_atual = date.today()
numero_mes = data_atual.month

nome_mes_completo = data_atual.strftime('%B')

print(nome_mes_completo)