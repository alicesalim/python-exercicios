n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
if m < 5:
    print('Você foi REPROVADO!')
elif m > 6.9:
    print('Você foi APROVADO!')
else:
    print('Você esta de recuperação!')
print('Sua média foi de {:.2f}.'.format(m))
