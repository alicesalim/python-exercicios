a = float(input('Digite seu salário: '))
if a > 1250:
    print('Seu salário teve um aumento de 10% e agora é igual a R${}'.format((a * 110) / 100))
else:
    print('Seu salário teve um aumento de 15% e agora é igual a R${}'.format((a * 1150) / 100))
