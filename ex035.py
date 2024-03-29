a = int(input('lado a: '))
b = int(input('lado b: '))
c = int(input('lado c: '))
if a < b + c and b < a + c and c < a + b:
    print('É possivel formar um triângulo')
else:
    print('Não é possivel formar um triângulo')
