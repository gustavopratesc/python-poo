# 29. Crie um programa em Python que calcule e escreva a soma dos números primos de 1 a
# 50.

lista = []

for n in range(1, 51):
    if n < 2:
        continue
    primo = True
    for i in range(2, n):
        if n % i == 0:
            primo = False
            break
    if primo:
        lista.append(n)

soma = sum(lista)
print(f'A soma dos números primos de 1 a 50 é {soma}')
