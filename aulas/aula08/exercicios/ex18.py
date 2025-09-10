# Crie um dicionário carrinho que guarda produtos (chave = nome) e valores (valor = preço).
# Calcule o preço total somando todos os valores usando values().
# Se o produto "Frete" não existir, adicione com valor 0.0 usando setdefault().

carrinho = {
    'Arroz': 10,
    'Feijão': 15.99,
    'Batata': 16.77,
    'Cenoura': 7,
    'Carne': 21
}

soma_valor = sum(carrinho.values())

print(f'Soma dos valores: R${soma_valor}')

if carrinho.get('Frete') is None:
    carrinho.setdefault('Frete', 0.0)

print(carrinho)

