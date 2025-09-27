# tupla e dicionarios

tupla = (10, 20, 30, 40, 50, 60, 70)

print(tupla[3:]) # fatiamento de tuplas

# tupla[1] = 50 # tupla é imutavel

# print(tupla)

tupla_inversa = sorted(tupla, reverse=True)
## ou

tupla_transformado_em_lista = list(tupla) # transformar tuplas em listas

print(tupla_inversa)
print(tupla[::-1])

frutas = ('Manga', 'Abacaxi', 'Limão', 'Maçã', 'Maçã')

print(f'Indica se a posição do valor: {frutas.count('Uva')}') # count
print(f'Conta os itens: {len(frutas)}') # len
print(f'{frutas.index('Maçã')}') # index
conjunto = set(frutas) # conjunto vai retirar os repetidos mas fica fora da ordem, fica em desordem
print(conjunto)


idades = (10, 22, 15, 21, 44)

print(f'Maximo das idades: {max(idades)}') # max
print(f'Minimo das idades: {min(idades)}') # min
print(f'Soma das idades: {sum(idades)}') # sum
idades_ordenadas = sorted(idades)
print(f'Idades ordenadas: {idades_ordenadas}') # sorted, mas tambem tem o sort
idades_ordenadas_reverso = sorted(idades, reverse=True) # usando o reverse=True
print(f'Idades ordenadas reversas: {idades_ordenadas_reverso}')