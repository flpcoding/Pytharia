tabelaBrasileirao2019: tuple[str] = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athetico-PR', 'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama', 'Atlétoco-MG', 'Fluminense', 'Botafogo', 'Ceará SC', 'CSA', 'Chapecoense', 'Avaí')

print(f'Os 5 primeiros são: {tabelaBrasileirao2019[:5]}')
print(f'Os 4 últimos são: {tabelaBrasileirao2019[-4:]}')
print(f'Times em ordem alfabética: {sorted(tabelaBrasileirao2019)}')


posChapecoense = tabelaBrasileirao2019.index('Chapecoense')

print(f'A Chapecoense está na {posChapecoense}ª posição.')

print('A Chapecoense está na {}ª posição.'.format(tabelaBrasileirao2019.index('Chapecoense')))

print(f'A Chapecoense está na {tabelaBrasileirao2019.index("Chapecoense")}ª posição.')
