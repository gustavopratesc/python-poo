# Crie um programa em Python que solicite ao usuário um número decimal e, em seguida,
# calcule e imprima o valor absoluto desse número. Usar o módulo math.

def valor_absoluto(number):
    return abs(number)

try: 
    numero = float(input('Insira um número: '))
    print(f'Valor absoluto do número {numero} é: {valor_absoluto(numero)}')
except ValueError:
    print('ERRO: Insira apenas números!')