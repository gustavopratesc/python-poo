def numeros_pares(n):
    if n % 2 == 0:
        for i in range(0, n, 2):
            print(f'Números pares: {i + 2}')
    else:
        print(f'Número inserido foi impar!')

try:
    numero = int(input('Digite ate o número que vc quer: '))
    numeros_pares(numero)
except ValueError:
    print('ERRO Valor inserido não é númerico!')