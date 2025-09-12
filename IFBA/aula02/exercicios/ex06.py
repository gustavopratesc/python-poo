# 6. Crie um programa em Python que leia um número e se este número for maior do que 20,
# imprima a metade dele

def numero_metade(numero):
    if numero > 20:
        return f'A metade desse número é {numero / 2}'
    else:
        return f'O número não vai ser repartido por 2!'

try:
    numero = int(input('Insira um número: '))
    print(numero_metade(numero))
except ValueError:
    print('ERRO: Insira apenas números!')