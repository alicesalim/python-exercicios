cores = {'vermelho':'\033[1;31m', 'verde':'\033[1;32m', 'normal':'\033[m'}
n = int(input('Digite um número: '))
a = n - 1
s = n + 1
print('O seu antecessor é {}{}{} e o seu sucesssor é {}{}{}'.format(cores['vermelho'], a, cores['normal'], cores['verde'], s, cores['normal']))
