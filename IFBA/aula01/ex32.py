'''32. Crie um programa em Python que leia a velocidade de um veículo numa estrada
retilínea e a velocidade de um outro veículo que esteja vindo no sentido oposto, e a
distância entre eles. Calcule e escreva o tempo necessário para que esses veículos se
encontrem. Considere as dimensões dos veículos desprezíveis.'''

def movimento_relativo(velocidade1, velocidade2, distancia):
    velocidade_relativa = velocidade1 + velocidade2
    tempo = distancia / velocidade_relativa
    print(f'Velocidade do 1° carro: {velocidade1}Km/h')
    print(f'Velocidade do 2° carro: {velocidade2}Km/h')
    print(f'Distancia inical: {distancia:.2f}')
    print(f'Tempo em que eles se encontrarão: {tempo:.2f}')



try:
    velocidade1 = float(input('Insira a velocidade do primeiro veiculo: '))
    velocidade2 = float(input('Insira a velocidade do segundo veiculo: '))
    distancia = float(input('Insira a distancia: '))
    movimento_relativo(velocidade1, velocidade2, distancia)
except ValueError:
    print('ERRO: Insira apenas números!')
