n = ('lapis', 1.00, 'borracha', 0.50)
for c in range(0, len(n)):
    if c % 2 == 0:
        print(f'{n[c]:.<30}', end=' ')
    else:
        print(n[c])
