import math
co = int(input('Cateto oposto: '))
ca = int(input('Cateto adjacente: '))
h = math.hypot(ca, co)
#h = math.sqrt(co ** 2 + ca ** 2)
print('A hipotenusa desse triângulo retângulo é {}'.format(h))

