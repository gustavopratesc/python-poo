def lista_de_quadrados(lista):
    lista_dobrada = [n ** 2 for n in lista] # <- list comprehension:
    return lista_dobrada
        

lista = []

try:
    qtd = int(input('Quer quantos números na lista?: '))

    for i in range(qtd):
        numero = int(input(f'Digite o {i + 1} número: '))
        lista.append(numero)

    print(f'Os quadrados da lista é {lista_de_quadrados(lista)}')

except ValueError:
    print('ERRO VALOR INSERIDO NÃO É NÚMERICO!')