# 20. Crie um programa em Python que declare duas variáveis inteiras e atribua a elas
# valores diferentes. Em seguida, utilize o operador ternário para imprimir o maior desses dois
# números.

n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))

resultado = f'N1° {n1} maior' if n1 > n2 else f'N2° {n2} maior'

print(resultado)