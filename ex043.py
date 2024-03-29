p = float(input('Digite seu peso em Kg: '))
h = float(input('Digite sua altura em M: '))
imc = p / (h * h)
print('Seu IMC é {:.2f}'.format(imc))
if imc < 18.5:
    print('ABAIXO DO PESO')
elif 18.5 <= imc <= 25:
    print('PESO IDEAL')
elif 25 < imc <= 30:
    print('SOBREPESO')
elif 30 < imc <= 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')
