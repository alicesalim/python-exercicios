x = cont = y = 0
v = int(input('Qual valor deseja sacar? '))
total = v
ced = 50
contced = 0
while True:
    if total >= ced:
        total -= ced
        contced += 1
    else:
        print(f'{contced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
    if ced == 0:
        break
