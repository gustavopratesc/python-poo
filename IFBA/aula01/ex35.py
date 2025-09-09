'''35. Crie um programa em Python que declare uma variável do tipo booleana e inicialize com
o resultado da comparação de desigualdade entre dois números inteiros. Imprima o valor
booleano resultante.'''


verdadeiro = False

numero1 = int(input('Insira o primeiro n1: '))
numero2 = int(input('Insira o segundo n2: '))

if numero1 == numero2:
    verdadeiro = True
    print(f'A variavel boolena que estava False virou True: {verdadeiro}')
elif numero2 == numero1:
    verdadeiro = True
    print(f'A variavel boolena que estava False virou True: {verdadeiro}')
else:
    print(f'A variavel ainda continua False: {verdadeiro}')