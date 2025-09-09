'''25. Crie um programa em Python que leia o nome e o peso de uma pessoa em kg e informe
a quantidade de água em litros, quantidade de carboidratos em g e quantidade de proteínas
em g, que ela deve ingerir diariamente, sendo que o recomendável é a ingestão de 50 ml de
água por kg corporal; 6 g de carboidratos por kg corporal; e 2,5 g de proteínas por kg
corporal.'''

def checkup_saude(nome, peso):
    if not nome:
        print('ERRO: Digite seu nome!')
        return
    print('-- RECOMENDAÇÕES --')
    quant_agua = (peso * 50) / 1000
    quant_carboidrato = peso * 6
    quant_proteina = peso * 2.5
    print(f'Quantidade de agua: {quant_agua:.2f} L')
    print(f'Quantidade de carboidrato: {quant_carboidrato:.2f} G')
    print(f'Quantidade de proteinas: {quant_proteina:.2f} P')


nome = str(input('Insira seu nome: ')).strip().title()
try:
    peso = float(input('Insira seu peso: '))
    checkup_saude(nome, peso)
except ValueError:
    print('ERRO: Insira apenas números!')