a = int(input('Digite a distância da viagem em Km: '))
if a <= 200:
    print('O valor da viagem é igual a R${}'.format(a * 0.5))
else:
    print('O valor da viagem é igual a R${}'.format(a * 0.45))
