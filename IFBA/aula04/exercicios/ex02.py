# 2. Peça ao usuário um valor N, crie uma lista contendo os quadrados dos números de 1 até
# N, e imprima essa lista.

lista_quadrados = []

try:
    numero = int(input('Insira um número: '))
    for i in range(1, numero + 1):
        quadrados = i ** 2
        lista_quadrados.append(quadrados)

    for n in lista_quadrados:
        print(f'{n}')

except ValueError:
    print('ERRO: Insira apenas números!')