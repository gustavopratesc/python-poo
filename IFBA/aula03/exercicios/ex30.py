
def soma_par_digitos(numero):
    soma = 0
    tem_par = False
    for n in str(numero):
        digito = int(n)
        if digito % 2 == 0:
            soma += digito
            tem_par = True
    if not tem_par:
        print('Não possui números pares')
    else:
        print(f'O resultado da soma dos digitos pares é {soma}')

try:
    numero = int(input('Insira um digitos de um número: '))
    soma_par_digitos(numero)
except ValueError:
    print('ERRO: Insira apenas números!')