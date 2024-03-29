valores = []
maior = 0
menor = 0
for v in range(0, 4):
    valores.append(int(input(f'Digite um valor para a posição {v}: ')))
    if v == 0:
        maior = menor = valores[v]
    else:
        if valores[v] > maior:
            maior = valores[v]
        if valores[v] < menor:
            menor = valores[v]
print(f'Você digitou os valores {valores}')
print(f'o maior valor é {maior} e esta na posição', end=' ')
for p, c in enumerate(valores):
    if c == maior:
        print(p)
print(f'O menor valor é {menor} e esta na posiçào', end=' ')
for p, c in enumerate(valores):
    if c == menor:
        print(p)
