dados = {
    'produto1': 20,
    'produto2': 30,
    'produto3': 'Caneta'
}

novo_dados = {chave: (valor * 2) if isinstance(valor, (int, float)) else valor.upper() for chave, valor in dados.items()}

print(novo_dados)