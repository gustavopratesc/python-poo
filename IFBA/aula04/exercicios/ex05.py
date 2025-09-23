# 5. Dada uma lista de números, encontre o segundo maior elemento presente
# (considerando que pode haver repetidos) e imprima.

def segundo_maior(lista):
    unicos = list(set(lista))
    if len(unicos) < 2:
        return None
    
    unicos.sort(reverse=True)
    return unicos[1]

lista_numeros = [1, 2, 66, 100, 100]
print(segundo_maior(lista_numeros))