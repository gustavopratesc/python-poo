# 9. Crie um programa em Python que calcule a soma dos números de 1 a 100.

lista = []

for i in range(1, 101):
    lista.append(i)

soma = sum(lista)

print(soma)