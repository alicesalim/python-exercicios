lista = []
r = ''
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
    else:
        print('Não vou adicionar pois este número ja esta na lista')
    r = str(input('Deseja continuar? [S/N] '))
    if r in 'Nn':
        break
print(f'lista: {lista}')
