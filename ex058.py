from random import randint
n = randint(0,10)
print('Eu pensei em um número entre 0 e 10.')
a = int(input('Qual número você acha que eu pensei? '))
while a != n:
    print('Você errou!')
    a = int(input('Tente novamente: '))
print('Você acertou!')
