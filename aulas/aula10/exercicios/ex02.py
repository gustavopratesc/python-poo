numeros = [10, 15, 22, 33, 40, 55, 60]

filtro = filter(lambda number: number % 5 == 0, numeros)

print(list(filtro))

maiores_que_30 = filter(lambda number: number > 30, numeros)

print(list(maiores_que_30))