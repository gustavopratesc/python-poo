# def maior_numero(lista):
#     print(f'O maior número é {max(lista)}')

# lista_numeros = []
# try:
#     for i in range(3):
#         numero = int(input(f'Insira {i + 1}° número: '))
#         lista_numeros.append(numero)
# except ValueError:
#     print('ERRO: Valor digitado não é númerico')

# maior_numero(lista_numeros)

##

def max_numero(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        print(f'O maior número é o {n1}')
    elif n2 > n1 and n2 > n3:
        print(f'O maior número é o {n2}')
    else:
        print(f'O maior número é o {n3}')


try:
    n1 = int(input('Insira o primeiro número: '))
    n2 = int(input('Insira o primeiro número: '))
    n3 = int(input('Insira o primeiro número: '))
    max_numero(n1, n2, n3)
except ValueError:
    print('ERRO: valor digitado não é inteiro númerico!')