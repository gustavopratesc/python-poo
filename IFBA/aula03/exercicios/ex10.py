# 10. Crie um programa em Python que imprima a soma dos quadrados dos números de 1 a
# 10.

lista = []

for i in range(1, 11):
    quadrados = i ** 2
    lista.append(quadrados)

soma = sum(lista)

print(soma)