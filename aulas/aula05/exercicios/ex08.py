def par_ou_impar(number):
    if number % 2 == 0:
        print(f'Esse número {number} é par!')
    else:
        print(f'Esse número {number} é impar!')


continuar = 'S'
while continuar in ['S', 'SIM']:
    print('-- PAR OU IMPAR --')
    try:
        numero = int(input('Digite um número: '))
        par_ou_impar(numero)
        continuar = input('Quer continuar? [S/N]: ').strip().upper()
    except ValueError:
        print(f'ERRO: Você digitou {numero} | É permitido apenas números interios!')