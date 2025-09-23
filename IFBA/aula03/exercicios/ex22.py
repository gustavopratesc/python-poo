# 22. Crie um programa em Python que peça ao usuário um número e imprima se é um
# número triangular ou não. (Ex: 1, 3, 6, 10, etc.).

def numero_triangular(numero):
    return numero * (numero + 1) // 2

for i in range(1, 6):
    print(f'{i}° número triangular = {numero_triangular(i)}')