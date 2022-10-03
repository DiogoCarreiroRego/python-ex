"""
Declare uma lista para guardar as vendas do grupo central
Declara uma lista para guardar os nomes das cinco ilhas do grupo central
Peça dados ao utilizador e guarde-os na lista
Após o utilizador ter inserido os 5 valores apresente:
- Total das vendas
- O menor valor inserido
- O maior valor inserido
- A média das vendas
"""
from builtins import sum

ilhas = ['Terceira', 'Graciosa', 'Pico', 'Faial', 'São Jorge']

if __name__ == '__main__':
    vendas = []
    for ilha in ilhas:
        vendas.append((int(input(f'Insira as vendas para {ilha} '))))
    print(f'vendas={vendas}')

    menor = vendas[0]
    maior = vendas[0]
    for x in range(1, len(vendas)):
        if vendas[x] < menor:
            menor = vendas[x]
        if vendas[x] > maior:
            maior = vendas[x]
    print(f'O maior é {maior} e o menor é {menor}.')
    print(f'O maior é {max(vendas)} e o menor é {min(vendas)}.')
    print(f'O maior é {sorted(vendas)[4]} e o menor é {sorted(vendas)[0]}.')

    total = 0
    for v in vendas:
        total += v

    media = total / len(vendas)


    print(f'O total é {sum(vendas)} e a média é {media}.')



"""
    continuar = 's'
    while continuar == 's':
        ini = int(input('Insira o número inicial '))
        fim = int(input('Insira o número final '))
        primos = 0
        for n in range(ini, fim + 1):
            if divisores(n) == 2:
                primos += 1
        print(f'Entre {ini} e {fim} há {primos} de primos.')
        continuar = input('Repetir [s | n]? ')
    print(f'Adeus!')
"""