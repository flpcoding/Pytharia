produtos: tuple[str, float] = ('pão', 1.5, 'arroz', 10.50)

for i, produto in enumerate(produtos):
    if i % 2 == 0:
        print(f'{produto:.<20}', end=' ')
    else:
        print(f'R$ {produto:>8.2f}')
