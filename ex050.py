soma = 0
cont = 0
for c in range(0,6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print('A soma dos {} números pares é igual a {}'.format(cont, soma))
