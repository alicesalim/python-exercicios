from datetime import date
ano = date.today().year
cont = 0
for c in range(0, 7):
    n = int(input('Em que ano a {}ª pessoa nasceu? '.format(c + 1)))
    if ano - n >= 18:
        cont += 1
print('Ao todo tivemos {} pessoas maiores de idade \nE também tivemos {} pessoas menores de idade'.format(cont, 7 - cont))
