lista = []
r = ''
cont = 0
while r in 'Ss':
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N] '))
    lista.append(n)
    cont += 1
    lista.sort(reverse=True)
print(20*'*')
print(f'Você digitou {cont} números')
print(f'Os valores digitados em ordem decrescente foram: {lista}')
if 5 in lista:
    print('O valor 5 foi encontrado!')
else:
    print('O valor 5 não foi encontrado!')
