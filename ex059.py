from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
a = 0
while a != 5:
    print('''[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')
    a = int(input('Qual a sua opção? '))
    if a == 1:
        print('A soma é {}'.format(n1 + n2))
    if a == 2:
        print('A multiplicação é {}'.format(n1 * n2))
    if a == 3:
        if n1 > n2:
            print('o maior é {}'.format(n1))
        else:
            print('O maior é {}'.format(n2))
    if a == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    if a > 5 or a < 1:
        print('Valor incorreto')
    print(50 * '*')
    sleep(1)
print('FIM')
