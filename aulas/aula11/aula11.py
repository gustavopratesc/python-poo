# empacotamento e desempacotamento

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza'
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6
}

pessoa_completa = {**pessoa, **dados_pessoa, 'chave': 156468}
print(pessoa_completa)

# args e kwargs
# args(ja vimos *)
# kwargs - keywords arguments (argumentos ja nomeados)

def mostro_argumentos_nomeados(*args, **kwargs):
    print(f'Não nomeados: {args}')

    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')


mostro_argumentos_nomeados(1, 2, 3, nome= 'Gustavo', idade= '21') # usa o igual = ou recebe

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4
}

mostro_argumentos_nomeados(**configuracoes)