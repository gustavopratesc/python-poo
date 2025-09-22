'''11. Crie um programa em Python que escreva a média de 10 números informados pelo
usuário'''

def media_usuario(lista):
    media = sum(lista) / len(lista)
    return media


contador = 1

lista_numeros = []

while contador <= 10:
    numero = float(input(f'Insira o {contador}° número: '))
    contador += 1
    lista_numeros.append(numero)

print(f'A media de números digitados é: {media_usuario(lista_numeros):.2f}')

## com for

lista_n_for = []

for i in range(10):
    n = float(input(f'Insira o {n}° numero: '))
    lista_n_for.append(n)


media = sum(lista_n_for) / len(lista_n_for)

print(media)