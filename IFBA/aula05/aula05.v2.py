# dicionario

pessoa = {
    'nome': 'Gustavo',
    'idade': 21,
    'cidade': 'Vitoria da Conquista',
    'curso': 'Sistemas de informação' 
}

print(pessoa['idade']) # printar a idade
print(pessoa['nome']) # printar o nome

pessoa['idade'] = 44

print(pessoa['idade'])

for k, v in pessoa.items():
    print(k, v)