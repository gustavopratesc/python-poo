# 31. Crie um programa em Python que leia uma quantidade de álcool em gramas, e escreva
# a quantidade de calorias que a substância precisa receber para atingir sua temperatura de
# autoignição, sabendo que a temperatura ambiente atual é de 25 graus Celsius

def autoignicao(alcool):
    c = 0.6        
    t_auto = 363   
    t_amb = 25     

    deltaT = t_auto - t_amb 

    calor_sensivel = alcool * c * deltaT

    print(f'A quantidade de calor necessária é: {calor_sensivel:.2f} calorias')


try:
    alcool = float(input('Insira a quantidade de álcool em gramas: '))
    autoignicao(alcool)
except ValueError:
    print('ERRO: Insira apenas números!')
