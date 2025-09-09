'''29. Num termômetro de mercúrio, a coluna liquida apresenta 0,4 cm quando em presença
do gelo em fusão e 20,4 cm quando em presença de água em ebulição. Crie um programa
em Python que leia a altura na coluna de mercúrio em cm e escreva a temperatura
equivalente na escala Celsius.'''

def escala_celsius(altura):
    temperatura = (5 * altura) - 2
    if altura < 0.4 or altura > 20.4:
        print('Atenção valor fora do intervalo de calibração!')
    else:
        print(f'A altura informada foi {altura} cm')
        print(f'A temperatura correspondente é: {temperatura} °C')


try:
    altura_coluna = float(input('Insira a altura da coluna: '))
    escala_celsius(altura_coluna)
except ValueError:
    print('ERRO: Digite apenas números!!')