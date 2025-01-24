lanche: tuple[str] = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
numeros: tuple[int] = (1, 2, 3, 3, 4, 1)
x = 1
# Tuplas são imutáveis
lanche[0] = 'Água'
print(lanche[2:])

for comida in lanche:
    print(comida, end=' ')
print('\n')

for i in range(0, len(lanche)):
    print(lanche[i])

for posicao, comida in enumerate(lanche):
    print(f'{posicao} - {comida}')

#
#   TUPLAS - MÉTODOS
#

print(numeros.count(3)) # Quantas vezes aquele elemeto ocorreu
print(lanche.index('Suco')) # Posição na tupla do parâmetro passado

del(lanche) # Apaga da memória o que está como argumento.
del(x)
print(lanche)
print(x)