cores = {'verm':'\033[31m', 'normal':'\033[m'}
a = int(input('Digite o número: '))
n = int(input('Para a conversão na base binária digite {}1{}, para base octal digite {}2{} e para base hexadecimal digite {}3{}: '.format(cores['verm'], cores['normal'], cores['verm'], cores['normal'], cores['verm'], cores['normal'])))
if n == 1:
    print('Base binária: {}'.format(bin(a)[2:]))
elif n == 2:
    print('Base octal: {}'.format(oct(a)[2:]))
elif n == 3:
    print('Base hexadecimal: {}'.format(hex(a)[2:]))
