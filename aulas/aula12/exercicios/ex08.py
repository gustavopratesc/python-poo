# Números divisíveis por 3
# Gere um conjunto com todos os números de 0 a 30 divisíveis por 3.

numeros_divisiveis = {x for x in range(0, 31) if x % 3 == 0}

print(numeros_divisiveis)