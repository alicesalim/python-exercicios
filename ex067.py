while True:
    n = int(input('Digite um número: '))
    if n < 0:
        break
    for c in range(0, 11):
        print(f'{n} x {c} = {n * c}')
