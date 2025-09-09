'''24. Crie um programa em Python que declare uma variável do tipo string e a inicialize com o
nome de uma pessoa em minúsculo. Posteriormente substitua um dos seus sobrenomes
por outro.'''

def substituir_sobrenome(sobrenome):
    outro_sobrenome = sobrenome.split()
    outro_sobrenome[1] = 'silva'
    print(*outro_sobrenome)


nome = str(input('Insira seu nome completo: ')).strip().lower()
if not nome:
    print('ERRO: INSIRA UM NOME!')
else:
    substituir_sobrenome(nome)