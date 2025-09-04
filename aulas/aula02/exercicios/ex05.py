def calc(a, b, operacao):
    if operacao == '+':
        return a + b
    elif operacao == '-':
        return a - b
    elif operacao == '*':
        return a * b
    elif operacao == '/':
        return a / b
    else:
        print('ERRO')

print(calc(10, 2, "+"))
print(calc(a=5, b=4, operacao="*"))
print(calc(4, 10, operacao="/"))