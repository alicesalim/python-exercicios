a = int(input('Digite um número: '))
c = a
f = 1
while c > 0:
    f *= c
    c -= 1
print('O fatorial desse número é {} '.format(f))
