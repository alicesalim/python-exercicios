a = float(input('Qual o valor da casa desejada? '))
b = float(input('Em quantos anos você deseja comprar a casa? '))
c = float(input('E qual o valor do seu salário? '))
parcela = a / (b * 12)
porcentagem = c * 0.3
if parcela <= porcentagem:
    print('Parabêns! Você podera comprar a casa com parcelas no valor de R${:.2f} por mês.'.format(parcela))
else:
    print('Você infelizmente nao podera comprar a casa, pois o valor das parcelas é superior a 30% do seu salário')
