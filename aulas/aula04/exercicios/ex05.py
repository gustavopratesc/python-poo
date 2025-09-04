def maior_numero(a, b, c):
    if a > b and a > c:
        return f'O primeiro número é maior'
    elif b > a and b > c:
        return f'O segundo número é maior'
    else:
        return f'O terceiro número é maior'

try:
    n1 = int(input('Insira o primeiro número: '))
    n2 = int(input('Insira o segundo número: '))
    n3 = int(input('Insira o terceiro número: '))
    print(maior_numero(n1, n2, n3))
except ValueError:
    print('ERRO: Valor digitado não é númerico!')
