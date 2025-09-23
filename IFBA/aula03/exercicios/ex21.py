# 21. Crie um programa em Python que leia uma quantidade de números de entrada e depois
# leia esses números, e ao final imprima o menor número lido.

try:
    quantidade_numeros = int(input('Digite quantos números você quer digitar: '))

    if quantidade_numeros <= 0:
        print('Digite uma quantidade maior que zero.')
    else:
        primeiro_numero = int(input('Insira o número: '))
        maior = primeiro_numero
        menor = primeiro_numero

        for i in range(quantidade_numeros - 1):
            numero = int(input('Insira o número: '))
            if numero > maior:
                maior = numero
            if numero < menor:
                menor = numero

        print(f'O maior número é: {maior}')
        print(f'O menor número é: {menor}')
except ValueError:
    print('ERRO: Valor inserido não é numérico!')
