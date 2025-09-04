def par_ou_impar(numero):
    if numero % 2 == 0:
        return f'Esse número {numero} é par!'
    else:
        return f'Esse número {numero} é impar!'
    
try:
    numero = int(input('Digite um número: '))
    print(par_ou_impar(numero))
except ValueError:
    print('ERRO: Valor digitado não é inteiro númerico!')