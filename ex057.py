a = str(input('Informe seu sexo: [M/F]  ')).strip().upper()[0]
while a not in 'MF':
        a = str(input('Dados inválidos. Informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado'.format(a))