# 18. Crie um programa em Python que solicite dois números ao usuário e imprima a soma de
# todos os números entre esses dois.

try:
    n1 = int(input('Insira o primeiro número: '))
    n2 = int(input('Insira o segundo número: '))
    resultado = 0
    for i in range(n1, n2 + 1):
        resultado += i
    print(resultado)
except ValueError:
    print('ERRO: Insira apenas números!')


## ou forma mais completa

try:
    n1 = int(input('Insira o primeiro número: '))
    n2 = int(input('Insira o segundo número: '))

    resultado = 0
    inicio = min(n1, n2)
    fim = max(n1, n2)

    for i in range(inicio, fim + 1):
        resultado += i

    print(f'A soma de todos os números entre {n1} e {n2} é {resultado}')
except ValueError:
    print('ERRO: Insira apenas números!')
