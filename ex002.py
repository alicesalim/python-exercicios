n = input('Qual o seu nome: ')
cores = {'amarelo':'\033[33m', 'normal':'\033[m'}
print('Seja bem vindo {}{}{}'.format(cores['amarelo'], n, cores['normal']))
