# 14. Crie um programa em Python que imprima a raiz quadrada de todos os números de 100
# até 1.

from math import sqrt

for i in range(100, 0, -1):
    print(f'{sqrt(i):.2f}')

    