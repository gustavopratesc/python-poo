'''33. Crie um programa em Python que leia o tempo (em segundos) que um objeto em queda
livre demora para atingir o solo, e escreva a altura da queda (em centímetros). Considere a
aceleração da gravidade = 9,8 m/s2, e desconsidere o atrito do ar.'''

def queda_livre(tempo):
    g = 9.8
    altura_metros = 0.5 * g * (tempo ** 2)
    altura_centimetros = altura_metros * 100
    print(f'A altura da queda é: {altura_centimetros:.2f} cm')

try:
    tempo = float(input('Insira o tempo em segundos: '))
    queda_livre(tempo)
except ValueError:
    print('ERRO Insira apenas números!')