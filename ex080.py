lista = []
maior = 0
menor = 0
for cont in range(0, 4):
    n = int(input('Digite um númmero: '))
    if cont == 0 or n > lista[len(lista)-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print(lista)
