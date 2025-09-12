# 4. Crie um programa em Python que solicite ao usuário o código de um produto e imprima a
# categoria dele: 1 a 10 (Alimentação), 11 a 20 (Limpeza), 21 a 30 (Eletrônicos).

def codigo_produto(numero_codigo):
    if 1 < numero_codigo <= 10:
        print('Alimentação')
    elif 11 < numero_codigo <= 20:
        print('Limpeza')
    elif 21 < numero_codigo <= 30:
        print('Eletronicos')
    else:
        print('Insira os números informados!')
        

print('''
    Codigos:
    1 a 10: (Alimentação)
    11 a 28: (Limpeza)
    21 a 30 (Eletrônicos)
''')

try:
    numero_codigo = int(input('Insira o número que quer acessar!: '))
    codigo_produto(numero_codigo)
except ValueError:
    print('ERRO: Digite apenas números inteiros!')