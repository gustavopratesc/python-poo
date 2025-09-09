# 28. Crie um programa em Python que leia uma temperatura definida na escala Fahrenheit,
# converta e escreve a temperatura equivalente na escala Kelvin.

def kelvin(temperatura):
    k = (temperatura - 32) * (5/9) + 273.15
    return k


try:
    fahrenheit = float(input('Insira a temperatura em F°: '))
    print(f'A temperatura em F {fahrenheit}° em K {kelvin(fahrenheit):.2f}°')
except ValueError:
    print('ERRO: DIGITE APENAS NÚMEROS INTEIROS')