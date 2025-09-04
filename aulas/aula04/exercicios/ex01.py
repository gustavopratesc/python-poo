def dobro(n):
    return 2 * n

try:
    numero = int(input('Digite um número: '))
    print(f'O dobro de {numero} é: {dobro(numero)}')
except ValueError:
    print('ERRO: Valor inserido não é inteiro númerico')

