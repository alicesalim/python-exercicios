cores = {'verm':'\033[1;31m','verd':'\033[1;32m', 'normal':'\033[m'}
n = int(input('Digite um valor: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {}{}{} é {}{}{}, o triplo é {}{}{} e a raiz quadrada é {}{:.3f}{}'.format(cores['verm'], n, cores['normal'], cores['verd'], d, cores['normal'], cores['verd'], t, cores['normal'], cores['verd'], r, cores['normal']))

