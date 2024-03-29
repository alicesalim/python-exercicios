from random import randint
cont = 0
while True:
    n1 = int(input('Digite um número: '))
    r = str(input('Impar ou Par [I/P]? ')).strip().lower()[0]
    n2 = randint(1, 10)
    tot = n1 + n2
    if tot % 2 == 0:
        print(f'Você jogou {n1} e o computador jogou {n2}, que juntos dão {tot} que é PAR')
        a = 'p'
    else:
        print(f'Você jogou {n1} e o computador jogou {n2}, que juntos dão {tot} que é IMPAR')
        a = 'i'
    if a == r:
        print('Você GANHOU"')
    cont += 1
    if a != r:
        break
print('Você PERDEU!')
print('JOGO ENCERRADO')
print(f'Você ganhou {cont} vezes')
