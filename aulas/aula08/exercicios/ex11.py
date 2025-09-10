def adicionar_chave(dic, chave, valor):
    dic[chave] = valor
    print(dic)


pessoa = {}

pessoa['nome'] = 'Gustavo'

adicionar_chave(pessoa, 'idade', 25)

def remover_chave(dic, chave):
    if chave in dic:
        del dic[chave]
        print(f'Chave: {chave} removida com sucesso')
    else:
        print(f'Chave: {chave} não encontrada')
    print(dic)

carro = {}

carro['ano'] = 1999

remover_chave(carro, 'ano')
remover_chave(carro, 'toyota')