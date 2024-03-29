n = ('ALICE', 'MUNIR', 'ANA CLAUDIA', 'YURI', 'LIDIO', 'MICHELINE')
for nome in n:
    print(f'{nome:<5}', end='  ')
    for a in nome:
        if a.lower() in 'aeiou':
            print(f'{a}', end=' ')
    print('')
