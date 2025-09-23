# 28. Crie um programa em Python que imprima os números primos de 1 a 50

for n in range(1, 51):
    if n < 2:
        continue
    primo = True
    for i in range(2, n):
        if n % i == 0:
            primo = False
            break
    
    if primo:
        print(n)

    