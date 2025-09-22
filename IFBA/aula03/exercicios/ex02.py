# 2. Crie um programa em Python que imprima todos os números pares entre 10 e 100.
print('FOR')
for i in range(10, 101, 2):
    print(i)

##
print()
print('while')
contador = 10

while contador <= 100:
    if contador % 2 == 0:
        print(contador)
    contador += 1