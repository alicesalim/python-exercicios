a = int(input('Digite o ano do seu nascimento: '))
i = 2023 - a
if i <= 9:
    print('Você é um atleta MIRIM.')
elif 9 < i <= 14:
    print('Você é um atleta INFANTIL.')
elif 14 < i <= 19:
    print('Você é um atleta JUNIOR.')
elif 19 < i <= 20:
    print('Você é um atleta SÊNIOR.')
else:
    print('Você é um atleta MASTER.')
