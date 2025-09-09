# 13. Crie um programa em Python que declare uma variável do tipo ponto flutuante e atribua
# a ela um valor. Em seguida, calcule e imprima a raiz cúbica desse valor

def raiz_cubica(number):
    raiz = number ** (1/3)
    print(f'A raiz cubica de {number} é: {raiz:.2f}')

try:
    numero = float(input('Insira um número: '))
    raiz_cubica(numero)
except ValueError:
    print('ERRO: Valor inserido não é númerico')