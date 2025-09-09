'''34. Crie um programa em Python que escreva a massa de um objeto gravitacional. Para
isso o usuário deve informar a distância dele a outro objeto gravitacional, a massa deste
outro objeto e a força gravitacional entre eles. Considere a constante gravitacional =
6,67408 ∙ 10-11 N.kg2/m2'''

def calcular_massa():
    CONSTANTE_GRAVITACIONAL = 6.67408e-11
    try:
        distancia = float(input('Insira a distancia entre os objetos: '))
        massa_do_outro_objeto = float(input('Insira a massa do outro objeto: '))
        forca_gravitacional = float(input('Insira a força gravitacional entre eles: '))


        massa1 = (forca_gravitacional * (distancia ** 2)) / (CONSTANTE_GRAVITACIONAL * massa_do_outro_objeto)

        print(f'A masssa do primeiro objeto gravitacional é {massa1:.2f} kg')
    
    except ValueError:
        print('ERRO: Insira apenas valores númericos!')
    except ZeroDivisionError:
        print('ERRO: A massa ou a constante não podem ser ZERO!')


calcular_massa()