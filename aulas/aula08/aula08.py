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

