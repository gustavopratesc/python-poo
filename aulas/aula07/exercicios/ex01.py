def criar_multiplicador(multiplicador):
    def multiplica(numero):
        return multiplicador * numero
    return multiplica

dobro = criar_multiplicador(2)
triplo = criar_multiplicador(3)

print(dobro(5))
print(triplo(5))