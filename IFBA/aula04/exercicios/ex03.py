# 3. Peça ao usuário um valor N, crie uma lista contendo os números de 1 até N em ordem
# inversa, e imprima.

def ordem_inversa(lista):
    lista_inversa = sorted(lista, reverse=True)
    return lista_inversa

lista_numeros = []

try:
    numero = int(input('Insira um número: '))
    for i in range(1, numero + 1):
        lista_numeros.append(i)
    
    print(f'A ordem inversa da lista é {ordem_inversa(lista_numeros)}')
except ValueError:
    print('ERRO: Insira apenas números inteiros!')