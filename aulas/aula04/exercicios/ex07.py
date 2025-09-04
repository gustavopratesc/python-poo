def divisao_segura(a, b):
    if b == 0:
        return 'ERRO: divisão por zero não permitida!'
    else:
        return a / b
    
n1 = int(input('Insira o númerador número: '))
n2 = int(input('Insira o dividendo número: '))

print(divisao_segura(n1, n2))