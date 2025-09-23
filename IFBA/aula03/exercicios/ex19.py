'''19. Crie um programa em Python que leia um intervalo inferior, e também um intervalo
superior e após calcule e imprima a soma dos número impares dentro desse intervalo.'''

lista_numeros_impar = []

try:
    intervalo_inferior = int(input('Insira um número com intervalo inferior: '))
    intervalo_superior = int(input('Insira um número com intervalo superior: '))
    for i in range(intervalo_inferior, intervalo_superior):
        if i % 2 == 1:
            lista_numeros_impar.append(i)
    soma_numeros = sum(lista_numeros_impar)

    print(f'A soma dos números impares dos intervalos é: {soma_numeros:.2f}')

except ValueError:
    print('ERRO: Insira apenas números inteiros!')