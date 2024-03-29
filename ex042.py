a = int(input('lado a: '))
b = int(input('lado b: '))
c = int(input('lado c: '))
if a < b + c and b < a + c and c < a + b:
    print('É possivel formar um triângulo')
    if a != b and b != c and a != c:
        print('O triângulo é escaleno')
    elif a == b and b == c and a == c:
        print('O triângulo é equilátero.')
    else:
        print('O triângulo é isósceles.')
else:
    print('Não é possivel formar um triângulo')
