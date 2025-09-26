# [expressão for item in iterável if condição]
lista_quadrados = [x**2 for x in range(1, 20) if x % 2 == 0]
#                  expressão / iteravel / condição  
print(lista_quadrados)
lista_set_quadrados = {x**2 for x in range(1, 20) if x % 2 == 0}
print(lista_set_quadrados)



