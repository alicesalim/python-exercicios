print(40*'=')
frase = '10 TERMOS DE UMA PA'
print('{:^40}'.format(frase))
print(40*'=')
n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
dez = n + (10 - 1) * r
for c in range(n, dez, r):
    print(c, end=' ➭')
print('FIM')