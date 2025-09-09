# 7. Crie um programa em Python que declare uma variável do tipo ponto flutuante e atribua a
# ela um valor informado pelo usuário. Em seguida, arredonde esse valor para duas casas
# decimais e imprima o resultado.

def arredondamento(number):
    print(f'Tirei as casas decimais desse número com :.1f: {number:.0f}')
    numero_inteiro = int(number)
    print(f'Removi as casas decimais transformando o número flutuante em inteiro: {numero_inteiro}')
    


try:
    numero = float(input('Digite um número flutuante: '))
    arredondamento(numero)
except ValueError:
    print(f'ERRO: Digite apenas números!')