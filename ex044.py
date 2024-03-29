cores = {'azul':'\033[34m', 'normal':'\033[m'}
v = float(input('Valor do produto: '))
p = int(input('''Para pagamento à vista no dinheiro/cheque digite {}1{} 
para pagamento à vista no cartão digite {}2{}
para pagamento em 2x no cartão digite {}3{}
para pagamento em 3x ou mais no cartão digite {}4{}
'''.format(cores['azul'], cores['normal'], cores['azul'], cores['normal'], cores['azul'], cores['normal'], cores['azul'], cores['normal'])))
if p == 1:
    a = v * 0.9
    print('O valor total com 10% de desconto é de R${}'.format(a))
elif p == 2:
    a = v * 0.95
    print('O valor total com 5% de desconto é de R${}'.format(a))
elif p == 3:
    a = v / 2
    print('O valor de cada parcela sera igual a R${}'.format(a))
elif p == 4:
    c = int(input('Em quantos meses deseja pagar? '))
    a = v * 1.2
    b = a / c
    print('O valor de cada parcela sera de R${}, com 20% de acrescimo no valor total do produto'.format(b))
else:
    print('***OPÇÃO DE PAGAMENTO INVALIDA***')
