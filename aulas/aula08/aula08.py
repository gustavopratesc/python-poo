'''Dicionarios em python (tipo dict)
Dicionarios são estruturas de dados tipo
par de "chave" e "valor"
chaves podem ser consideradas como "indice"
que vimos na lista e podem ser tipos mutaveis
como: str, int, float, bool
O valor pode ser qualquer tipo, incluindo outro dicionario
Usamos {} para criar dicionario

'''

pessoa = {
    "nome": 'Luiz Otavio',
    "sobrenome": 'Miranda',
    "idade": 18,
    "altura": 1.8,
    "endereços": [
        {"rua": 'tal tal', "numero": 123},
        {"rua": 'outra rua', "numero": 456}
    ]
}

print(pessoa, type(pessoa))
print(pessoa["endereços"][0]["rua"])

for chave in pessoa:
    print(chave)

# forma de acresentar novos endereços

novo_endereco = {"rua": "nova rua", "numero": 789}

pessoa["endereços"].append(novo_endereco)

'''Manipulando chaves e valores em dicionarios'''

pessoa['telefone'] = 77988529963

del pessoa["sobrenome"] # <- vai apagar o sobrenome da pessoa
print(pessoa)

if pessoa.get('sobrenome') is None: # get() e o None verifica se a chave existe no dicionario
    print('Não existe')
else:
    print(pessoa["sobrenome"])

'''Metodos uteis em dicionarios Python
len - quantas chaves
keys - iteravel com as chaves
values - iteravel com os valores
items - iteravel com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma copia rasa (shallow copy)
get - obtem uma chave
pop - Apaga um item com a chave especificada (del)
popitem - Apaga o ultimo item adicionado
update - Atualiza um dicionario com outro
'''

print(len(pessoa)) # quantas chaves
print(pessoa.keys()) # mostra as chaves
print(pessoa.values()) # mostra os valores
print(pessoa.items()) # mostra os items (chaves: valores)
pessoa.setdefault('idade', 0) # cria um valor padrão para chave idade se não tiver

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2]
}

print(d1)

d2 = d1.copy() # copia rasa se quiser algo mais completo use o import copy | deepcopy

d2['l1'][1] = 9999

print(d2)

p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda'
}

print(p1.get('nome', 'Não existe')) # obtem a chave se não tiver obtem o padrão None

nome = p1.pop('nome')
print(nome)
print(p1)

ultima_chave = p1.popitem() # popitem remove a ultima chave do dicionario
print(ultima_chave)
print(p1)


p1.update( # update vai atualizar o seu dicionario ou vai adicionar novas chaves ou valores
    {
        'nome': 'novo valor',
        'idade': 30,
    }
)
## ou pode fazer desse jeito
p1.update(nome='novo valor', idade=30)

print(p1)