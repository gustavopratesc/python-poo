def operacao(a, b, operacao):
    if operacao == 'soma':
        return a + b
    elif operacao == 'multiplicação':
        return a * b
    
def executa(funcao):
    return funcao


print(executa(operacao(5, 2, 'multiplicação')))