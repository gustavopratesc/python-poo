'''8. Crie um programa em Python que leia 5 números e imprima o quadrado de cada um
deles.'''

for i in range(1, 6):
    n = int(input('Insira o número: '))
    quadrado = n ** 2
    print(f'O quadrado desse número {n} é: {quadrado}')