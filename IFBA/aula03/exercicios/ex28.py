# 32. Crie um programa em Python que solicite números ao usuário até que ele informe um
# número negativo, então imprima a soma dos números digitados.

soma = 0

while True:
    numero = int(input('Digite um número se for negativo ira parar e retornar a soma: '))
    if numero < 0:
        print('Finalizando...')
        print(f'Resultados')
        print(f'Soma: {soma}')
        break
    soma += numero
