import random
from time import sleep
a = int(input('Escolha pedra(1), papel(2) ou tesoura(3): '))
lista = ['1', '2', '3']
b = int(random.choice(lista))
print('O computador escolheu {}'.format(b))
print('Calculando')
sleep(1)
print('...')
sleep(3)
if a == 1 and b == 3:
    print('Você ganhou!')
elif a == 1 and b == 2:
    print('Você perdeu!')
elif a == 2 and b == 1:
    print('Você ganhou!')
elif a == 2 and b == 3:
    print('Você perdeu!')
elif a == 3 and b == 1:
    print('Você perdeu!')
elif a == 3 and b == 2:
    print('Você ganhou!')
elif a == b:
    print('EMPATE!')
