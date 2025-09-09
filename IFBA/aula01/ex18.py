# 18. Crie um programa em Python que dados os valores de a, b e c referentes a equação de
# segundo grau, ax2 + bx + c = 0, forneça as raízes dessa equação. Considere que os valores
# de a, b, c sempre geraram um delta positivo. Usar o módulo math

import math

def equacao(a, b, c):

    if a == 0:
        print('ERRO: O valor de a não pode ser 0 em uma equação de segundo grau!')
        return # <-- para encerar a função 

    delta = math.pow(b, 2) - (4 * a * c)
    if delta > 0:         
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f'A equação possui duas raizes iguais e destintas')
        print(f'O valor de x1 ficou: {x1:.2f}')
        print(f'O valor de x2 ficou: {x2:.2f}')
    elif delta == 0:
        x1 = -b / (2 * a)
        print(f'A equação possui duas raizes reais e iguais')
        print(f'O valor de x1 e x2 é {x1:.2f}')
    else:
        print(f'O delta é {delta:.2f}')
        print('A equação não possui raizes iguais')

print('-- EQUAÇÃO SEGUNDO GRAU --')
try:
    a = float(input('Insira um número para a: '))
    b = float(input('Insira um número para b: '))
    c = float(input('Insira um número para c: '))
    equacao(a, b, c)
except ValueError:
    print('ERRO: Digite apenas números!')