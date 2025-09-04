"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
""" *args é uma tupla mas tem como converter em lista usando
    args = list(args)
 """
# Lembre-te de desempacotamento
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

def soma(*args):
    total = 0
    for numero in args:
        total += numero
        print(numero, total)


soma(1, 2, 3, 4, 5, 6)