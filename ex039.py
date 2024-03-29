n = str(input('Qual o seu nome? ')).strip().title()
a = int(input('Em que ano você nasceu? '))
i = 2023 - a
if i == 18:
    print('Já esta na hora de você se alistar!')
elif i > 18:
    print('Ja passou da hora de você se alistar. Você esta {} anos atrasado.'.format(i - 18))
else:
    print('Faltam {} anos para você se alistar.'.format(18 - i))
