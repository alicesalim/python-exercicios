n = cont = s = 0
while True:
    n = int(input('Digite um valor (99 para parar): '))
    cont += 1
    s += n
    if n == 999:
        break
print(f'Você digitou {cont} e a soma entre eles foi{s}')
