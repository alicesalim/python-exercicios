v = int(input('Digite a velocidade do carro: '))
m = (v - 80) * 7
if v > 80:
    print('Você foi multado no valor de {}'.format(m))
