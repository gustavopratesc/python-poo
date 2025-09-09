# 22. Crie um programa em Python que declare uma variável do tipo string e a inicialize com o
# nome de uma pessoa em minúsculo. Em seguida imprima quantos caracteres ela tem.

nome = str(input('Insira seu nome: ')).strip().lower()
if not nome:
    print('ERRO: Digite um nome!')
    
nome_sem_espaco = nome.replace(' ', '')
print(f'Seu nome é {nome} | Quantidade de caracteres: {len(nome_sem_espaco)}')