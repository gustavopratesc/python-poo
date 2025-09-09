'''30. Sabendo que uma determinada barra de cobre tem 90 metros a 0 oC, crie um programa
em Python que leia a temperatura atual em oC e indique o comprimento atual da barra, em
metros. Considere que α = é o coeficiente de dilatação linear, que para o cobre é de
1,7∙10-5 oC-1 ,'''

try:
    temperatura = float(input('Digite a temperatura: '))
    l0 = 90.0
    alpha = 1.7e-5

    delta = alpha * l0 * temperatura
    l = l0 + delta
    if temperatura > 0:
        print('Expansão dectada')
    elif temperatura < 0:
        print('Contração dectada')
    else:
        print('Sem variação (referência 0 C°)')
    
    print(f'Comprimentro inicial (L0): {l0:.2f} m')
    print(f'Variação DeltaL: {delta:.2f} m')
    print(f'Comprimento atual: {l:.2f} m')


except ValueError:
    print('ERRO: Digite apenas números!')


