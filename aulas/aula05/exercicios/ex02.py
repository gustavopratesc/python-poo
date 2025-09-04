def contar(*args):
    contador = len(args)
    return contador


numeros = []

while True:
    numero = int(input('Insira um número: '))
    numeros.append(numero)
    
    while True:  # loop interno só para validar a resposta
        continuar = input('Quer continuar? [S/N]: ').strip().upper()
        if continuar in ['S', 'SIM']:
            break  # volta pro loop externo
        elif continuar in ['N', 'NAO', 'NÃO']:
            print('Respostas!')
            print(contar(*numeros))
            fim = True   # flag de controle
            break
        else:
            print('Digite apenas [S/N]')
    
    if 'fim' in locals() and fim:  # verifica a flag 
        break # <-- para finalizar sem usar o exit()