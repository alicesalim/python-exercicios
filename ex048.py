soma = 0
cont = 0
for c in range(3, 500, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print('A soma dos {} valores é igual a {}'.format(cont, soma))
