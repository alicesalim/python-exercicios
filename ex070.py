tot = caro = cont = barato = 0
nomebarato = ''
while True:
    n = str(input('Nome do produto: ')).strip().title()
    p = float(input('Valor do produto: '))
    m = str(input('Mais algum produto [S/N]? ')).strip().lower()[0]
    cont += 1
    tot += p
    if p > 1000:
        caro += 1
    if cont == 1 or p < barato:
        barato = p
        nomebarato = n
    if m == 'n':
        break
print(f'O total da compra foi de R${tot}\n{caro} produtos foram mais de R$1000\nO produto mais barato ' +
      f'foi o {nomebarato} que custou R${p}')
