# 23. Crie um programa em Python que imprima a sequência de Fibonacci até o décimo
# termo.

def fibonacci(numero):
    a, b = 0, 1
    for _ in range(numero):
        a, b = b, a + b
    return a

for i in range(10):
    print(f'{i} = {fibonacci(i)}')