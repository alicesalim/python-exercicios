par = []
impar = []
lista =[]
r = ''
while r in 'Ss':
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    r = str(input('Quer contiuar? [S/N] '))
lista.append(impar)
lista.append(par)
print(f'A lista completa é: {lista}')
print(f'Os números pares são: {par}')
print(f'Os números impares foram: {impar}')
