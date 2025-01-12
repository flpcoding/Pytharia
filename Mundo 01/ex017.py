from math import hypot

catetoOposto = float(input('Cateto oposto: '))
catetoAdjacente = float(input('Cateto adjacente: '))

print(f'O triângulo retângulo terá a hipotenusa de {hypot(catetoOposto, catetoAdjacente) :.2f}')
