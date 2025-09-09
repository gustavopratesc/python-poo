# 27. Crie um programa em Python que leia uma temperatura definida na escala Celsius,
# converta e escreve a temperatura equivalente na escala Fahrenheit.

def fahrenheit(temperatura):
    f = (temperatura * (9/5)) + 32
    return f


try:
    celcius = float(input('Insira a temperatura em C°: '))
    print(f'A temperatura em C {celcius}° em F {fahrenheit(celcius):.2f}°')
except ValueError:
    print('ERRO: Insira apenas números!')