def soma(a, b):
    s = a + b
    return s
try:
    n1 = int(input('Insira o primeiro número: '))
    n2 = int(input('Insira o segundo número: '))
    print(f'A soma entre {n1} + {n2} = {soma(n1, n2)}')
except ValueError:
    print('ERRO: Nenhum valor digitado!')
