import random
n = random.randint(1, 10)
a = int(input('Tente adivinhar o número q eu pensei entre 1 e 10: '))
if n == a:
    print('Você acertou')
else:
    print('Você errou, o número era {}'.format(n))
