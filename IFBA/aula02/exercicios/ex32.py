# 32. Crie um programa em Python que calcule leia a altura e o peso de uma pessoa e calcule
# o seu IMC, indicando se ela está abaixo do peso(menor que 25) , com o peso normal (entre
# 20 e 25), com sobrepeso (entre 25 e 30) ou obeso (acima de 30).

def imc(peso, altura):
    imc = peso / (altura * altura)
    if imc < 18.5:
        return f'Abaixo do peso | imc: {imc:.2f}'
    elif 18.5 <= imc < 25:
        return f'Peso normal | imc: {imc:.2f}'
    elif 25 <= imc < 30:
        return f'Sobrepeso | imc: {imc:.2f}'
    else:
        return f'Obeso | imc: {imc:.2f}'


print('-- CALCULADORA DE IMC --')
try:
    peso = float(input('Insira o seu peso: '))
    altura = float(input('Insira a sua altura: '))
    print(imc(peso, altura))
except ValueError:
    print('ERRO: Digite apenas números!')