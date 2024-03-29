n = str(input('Digite um texto: ')).lower().strip()
print('A letra a aparece {} vezes'.format(n.count('a')))
print('A primeira vez foi na posição {}'.format(n.find('a')+1))
print('A última vez foi na posição {}'.format(n.rfind('a')+1))
