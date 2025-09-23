# 6. Em uma lista de números, calcule e mostre a soma de todos os elementos.


def soma_elementos(lista):
    return sum(lista)

def continuar():
    """Pergunta ao usuário se quer continuar. 
       Retorna True para continuar, False para parar."""
    while True:
        resp = input('Quer continuar? [S/N]: ').strip().upper()
        if resp in ['SIM', 'S']:
            return True   
        elif resp in ['NÃO', 'NAO', 'N']:
            return False  
        else:
            print('Digite entre [S/N]')

lista_numeros = []

try:
    while True:
        numero = float(input('Insira um número: '))
        lista_numeros.append(numero)
        if not continuar():  
            print('respostas...')
            print('Soma dos números:', soma_elementos(lista_numeros))
            break
except ValueError:
    print('ERRO: Digite apenas números!')
