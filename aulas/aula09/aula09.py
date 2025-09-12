"""
Sets - Conjuntos em Python (tipo set)
Conjuntos são ensinados na matematica
Representados graficamente pelo diagrama de Venn
Sets em Python são mutaveis, porem aceitam apenas tipos imutaveis como valor interno

Criando um set
set(iteravel) ou (1, 2, 3)

Sets são eficientes para remover valores duplicados de iteraveis
- eles não tem indexes
- eles não garantem ordem
- eles são iteraveis (for, in, not, in)

Metodos uteis:
add, update, clear, discard

"""

s1 = set()
s1 = {'Luiz', 1, 2, 3}

s1.add('Gustavo')

s1.update(('Olá mundo', 1, 2, 3))
# s1.clear() # vai limpar o set
s1.discard('Olá mundo') # <-- vai emilinar o valor especifico do set
print(s1)

'''
Operadores uteis:
união | união (union) - Une
intersecção & (intersection) - Itens presentes em ambos
diferença - Itens presentes apenas no set da esquerda
diferença simétrica - Itens que não estão em ambos

'''

s1 = {1, 2, 3}
s2 = {2, 3, 4}

s3 = s1 | s2 # união
s3 = s1 & s2 # intersecção (Itens presentes em ambos)
s3 = s2 - s1 # diferença (Itens apenas no set da esquerda)
s3 = s1 ^ s2 # diferença simetrica (itens que estão em ambos)
print(s3)


# exemplo de uso de SETS

letras = set()

while True:
    letra = input('Digite: ')
    letras.add(letra)

    if 'l' in letras:
        print('Acertou!!')
        break

    print(letras)