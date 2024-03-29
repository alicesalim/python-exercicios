a = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete')
n = int(input('Digite um número entre 0 e 10: '))
while n > 10:
    print('número errado')
    n = int(input('Tente novamente: '))
print(a[n])
