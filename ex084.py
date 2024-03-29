dados = []
lista = []
cont = 0
r = ''
maior = menor = 0
while r in 'Ss':
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    r = str(input('Quer continuar? [S/N] '))
    if cont == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        elif dados[1] < menor:
            menor = dados[1]
    lista.append(dados[:])
    dados.clear()
    cont += 1
print(f'{cont} pessoas foram cadastradas')
print(f'O maior peso foi {maior}')
print(f'O menor peso foi {menor}')
