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

print(f'Sobrenome da pessoa: {pessoa["sobrenome"]}')
print(f'Número da segunda residencia: {pessoa["endereços"][1]['numero']}')

novo_endereco = {"rua": "nova rua", "numero": 789}

pessoa["endereços"].append(novo_endereco)

print(pessoa['endereços'])

pessoa["idade"] = 25

print(pessoa)

pessoa["profissao"] = "programador"

print(pessoa)