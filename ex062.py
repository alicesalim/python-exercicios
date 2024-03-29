print('GERADOR DE PA')
print(20*'*')
a = int(input('Primeiro termo: '))
r = int(input('Razão: '))
t = a
cont = 1
tot = 0
mais = 10
while mais != 0:
    tot = tot + mais
    while cont <= tot:
        print('{}'.format(t), end=' ')
        t += r
        cont += 1
    print('PAUSA')
    mais = int(input('Mais quantos termos você quer? '))
    if mais == 0:
        print('Progressão finalizada')
        print('Foram mostrados {} termos'.format(tot))
