ci = cs = cm = 0
while True:
    print(' ')
    print(30*'*', 'CADASTRE UMA PESSOA', 30*'*')
    print(' ')
    i = int(input('Quantos anos vc tem? '))
    s = str(input('Qual seu sexo [F/M]? ')).strip().lower()[0]
    if i >= 18:
        ci += 1
    if s == 'm':
        cs += 1
    if i < 20 and s == 'f':
        cm += 1
    a = str(input('Deseja continuar [S/N]? ')).strip().lower()[0]
    if a == 'n':
        break
print(' ')
print(81*'*')
print(' ')
print(f'Ao total são {ci} pessoas maiores de idade \nTem {cs} homens \nE {cm} mulheres com menos de 20 anos. ')
