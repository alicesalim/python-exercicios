from random import randint
maior = 0
menor = 100
print('Os números sorteados foram: ')
for c in range(0, 5):
    a = randint(0, 100)
    n = a
    print(n, end=' - ')
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print(f'\nMaior: {maior}')
print(f'Menor: {menor}')
