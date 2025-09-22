'''5. Crie um programa em Python que imprima os números de 1 a 100, mas substitua os
múltiplos de 3 por "Fizz" e os múltiplos de 5 por "Buzz".
'''

for i in range(1, 101):

    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
