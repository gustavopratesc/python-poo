# 26. Crie um programa em Python que leia uma temperatura definida na escala Fahrenheit,
# converta e escreve a temperatura equivalente na escala Celsius.

def celcius(temperatura):
    c = (temperatura - 32) * (5/9)
    return c



try:
    fahrenheit = float(input('Insira a temperatura em F°: '))
    print(f'A temperatura em F°{fahrenheit} em C°{celcius(fahrenheit):.2f}')
except ValueError:
    print('ERRO iNSIRA APENAS NÚMEROS!')