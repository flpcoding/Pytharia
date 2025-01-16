maiorPeso = float(input('Informe o peso (KG): '))
menorPeso = maiorPeso

for i in range(0, 4):
    peso = float(input('Informe o peso (KG): '))
    if peso >= maiorPeso:
        maiorPeso = peso
    
    if peso <= menorPeso:
        menorPeso = peso

print(maiorPeso, menorPeso)