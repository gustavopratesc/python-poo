# 8. Multiplique cada elemento de uma lista por um valor específico fornecido pelo usuário.
# Mostre a lista antes e depois da multiplicação.

lista_numeros = [1, 10, 14, 44, 55, 99]
lista_nova = []
try:
    multiplicador = int(input('Insira o multiplicador: '))
    for n in lista_numeros:
        resultado = n * multiplicador
        lista_nova.append(resultado)
    
    print(lista_numeros)
    print(lista_nova)
except ValueError:
    print('ERRO: Insira apenas números inteiros!')