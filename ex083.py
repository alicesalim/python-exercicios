n = str(input('Digite uma expressão: '))
pilha = []
simb = ''
if simb in n:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
if len(pilha) == 0:
    print('expressão válida')
else:
    print('expressão inválida')
 ERRO
