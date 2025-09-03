def calculadora_simples(n1, n2, operacao):
    if operacao == '+':
        resultado = n1 + n2
        return resultado
    elif operacao == '-':
        resultado = n1 - n2
        return resultado
    elif operacao == '*':
        resultado = n1 * n2
        return resultado
    elif operacao == '/':
        resultado = n1 / n2
        return resultado
    else:
        print('ERRO: Digite entre (+ - * /)')

try:
    n1 = float(input('Insira o 1° número: '))
    n2 = float(input('Insira o 2° número: '))
    operacao = input('Insira entre (+ - * /): ')
    if not operacao:
        print('ERRO: Nenhum valor digitado!')
    else:
        print(f'O resultado é: {calculadora_simples(n1, n2, operacao)}')
except ValueError:
    print('ERRO: O valor inserido não é númerico')