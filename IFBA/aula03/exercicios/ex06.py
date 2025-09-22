# 6. Crie um programa em Python que imprima os números de 1 a 50, que sejam múltiplos de
# 3 e 7 ao mesmo tempo

for i in range(1, 51):
    if i % 3 == 0 and i % 7 == 0:
        print(i)