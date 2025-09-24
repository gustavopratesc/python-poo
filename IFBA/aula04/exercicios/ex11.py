# 11. Encontre e imprima a média (aritmética) dos elementos de uma lista.
# funcções
def media(lista_numeros):
    media = sum(lista_numeros) / len(lista_numeros)
    return media

def continuar():
    while True:
        continuar = input('Quer continuar?: [S/N]: ').strip().upper()
        if continuar in ['SIM', 'S']:
            return True
        elif continuar in ['NÃO', 'NAO', 'N']:
            return False
        else:
            print('Digite entre [S/N]!')


# programa principal
lista_numeros = []
while True:
    numero = int(input('Insira um número para a lista: '))
    lista_numeros.append(numero)
    if not continuar():
        print('-- MEDIA DOS NÚMEROS PASSADOS --')
        print(f'{media(lista_numeros):.2f}')
        break

