def criar_desconto(taxa):
    def desconto(preco):
        return preco - (preco * taxa)
    return desconto

desconto10 = criar_desconto(0.1)
desconto25 = criar_desconto(0.25)

print(desconto10(100))
print(desconto25(150))