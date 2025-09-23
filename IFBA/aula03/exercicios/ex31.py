# 35. Crie um programa em Python que peça ao usuário um número e imprima os seus
# dígitos em ordem inversa

lista_numeros = []

while True:
    numero = int(input('Insira um número: '))
    lista_numeros.append(numero)
    continuar = input('Quer continuar? [S/N]: ').strip().upper()
    if continuar in ['NÃO', 'NAO', 'N']:
        print('Resultados...')
        lista_inversa = sorted(lista_numeros, reverse=True)
        print(lista_inversa)
        break