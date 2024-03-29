num = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        num[l][c] = (int(input(f'Digite um valor para [{l}, {c}]: ')))
for l in range(0, 3):
    for c in range(0, 3):
        print(num[l][c], end='  ')
    print()
