r = cont = s = menor = maior = 0
while r != 'n':
    a = int(input('Digite um número: '))
    r = str(input('Quer continuar?[S/N] ')).lower().strip()[0]
    cont += 1
    s += a
    if cont == 1:
        maior = menor = a
    else:
        if a > maior:
            maior = a
        if a < menor:
            menor = a
m = s / cont
print('Você digitou {} números e a média foi {}'.format(cont, m))
print('O maior foi {} e o menor foi {}'.format(maior, menor))
