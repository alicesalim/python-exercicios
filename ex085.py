num = [[], []]
n = 0
for c in range(0, 5):
    n = int(input(f'Digite o {c+1} valor: '))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
num[0].sort()
num[1].sort()
print(f'Pares: {num[0]}')
print(f'Impae: {num[1]}')
