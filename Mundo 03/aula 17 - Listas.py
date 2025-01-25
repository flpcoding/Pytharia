x: list[int] = [1, 2, 3, 4, 5]
y: list[int] = x # Faz uma ligação a lista X
z: list[int] = list(x)
w: list[int] = x[:] # Faz uma cópia da lista X
# w: list[int] = x.copy() # Faz uma cópia da lista X

print(id(x)) # Id() - Mostra o endereço na memória
print(id(y))
print(id(w))

print('-'*20)
y[0] = 9
print(y)
x.append(6) # Adiciona o parâmetro na lista
print(x)
print(z)
print(w)

print('-'*20)
x.sort() # Organiza a lista
print(x)

x.sort(reverse=True) # Organiza a lista ao contrário
print(x)

print('-'*20)
x.pop() # Remove último elemento
x.pop(2) # Remove segundo elemento

print(x)

print('-'*20)
x.insert(0, 7) # Adiciona 7 na posição 0 da lista
x.insert(3, 7) # Adiciona 7 na posição 3 da lista
print(x)

print('-'*20)
x.remove(7) # Remove o primeiro 7 que encontrar
print(x)


