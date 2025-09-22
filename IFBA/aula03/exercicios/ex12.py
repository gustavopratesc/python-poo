# 12. Crie um programa em Python que leia uma quantidade de números, e em seguida leia
# esses números e imprima a média deles.


def media_numeros(lista):
    media = sum(lista) / len(lista)
    return media

lista_numeros = list()

try:
    quantidade_numeros = int(input('Insira uma quantidade de números para a lista: '))
    for i in range(quantidade_numeros):
        numero = float(input(f'Insira o {i + 1}° número: '))
        lista_numeros.append(numero)
    
    print(f'A media dos números é: {media_numeros(lista_numeros):.2f}')

except ValueError:
    print('ERRO: Insira apenas números inteiros!')

    