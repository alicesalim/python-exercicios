num = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
lista = []
s = somacoluna = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        num[l][c] = (int(input(f'Digite um valor para [{l}, {c}]: ')))
for l in range(0, 3):
    for c in range(0, 3):
        print(num[l][c], end='  ')
        if num[l][c] % 2 == 0:
            s += num[l][c]
    print()
print(f'{s}')
for l in range(0, 3):
    somacoluna += num[l][2]
print(somacoluna)
for c in range(0, 3):
    if c == 0:
        maior = num[1][c]
    elif num[1][c]:
        maior = num[1][c]
print(maior)
