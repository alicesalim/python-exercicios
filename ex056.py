m = 0
v = 0
mulher = 0
nome = ''
for c in range(0, 4):
    print('_____ {}ª PESSOA _____'.format(c + 1))
    n = str(input('Nome: ')).strip().title()
    i = int(input('Idade: '))
    s = str(input('Sexo [M/F]: ')).strip().upper()
    m += i
    if c == 1 and s in 'M':
        v = i
        nome = n
    if s in 'M' and i > v:
        v = i
        nome = n
    if s in 'F' and i < 20:
        mulher += 1
print('A média das idades é {} anos'.format(m / 4))
print('O homem mais velho tem {} anos e se chama {}'.format(v, nome))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulher))
