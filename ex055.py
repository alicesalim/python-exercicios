maior = 0
menor = 0
for c in range(0, 5):
    peso = float(input('Digite o peso da {}ª pessoa'.format(c + 1)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi {}Kg e o menor {}'.format(maior, menor))
