print(' ')
times = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense', 'Athletico-PR',
         'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco', 'Bahia', 'Santos',
         'Goiás', 'Coritiba', 'América-MG')
print(f'lista de times Brasileirão 2023: {times}')
print(' ')
print('Os 5 primeiros são:')
for c in range(0, 5):
    print(times[c], end=' - ')
print('\n  ')
print('Os 4 últimos são:')
for c in range(-5, -1):
    print(times[c], end=' - ')
print('Times em ordem alfabética:')
timesabc = tuple(sorted(times))
print(f'{timesabc}')
