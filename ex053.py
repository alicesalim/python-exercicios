a = str(input('digite uma frase: ')).replace(' ', '').upper()
i = ''.join(reversed(a))
print('O inverso de {} é {}'.format(a, i))
if a == i:
    print('A frase é um PALÍNDROMO')
else:
    print('A frase NÃO é um palíndromo')
