"""
Declare uma lista para guardar as vendas do grupo central
Declara uma lista para guardar os nomes das cinco ilhas do grupo central
Peça dados ao utilizador e guarde-os na lista
Após o utilizador ter inserido os 5 valores apresente:
- Total das vendas
- O menor valor inserido assim como as respetivas ilhas
- O maior valor inserido assim como as respetivas ilhas
- A média das vendas
"""

#print(chr(ord('A') + 32))

if __name__ == '__main__':
    vendas = []
    ilhas = ['Terceira', 'Graciosa', 'Pico', 'Faial', 'São Jorge']

    for ilha in ilhas:
        vendas.append(int(input(f'Qual é o número de vendas para {ilha}? ')))

    total_vendas = 0
    for x in vendas:
        total_vendas += x

    media_vendas = total_vendas / len(vendas)

    print(f'O total de vendas é {total_vendas}')
    print(f'A média de vendas é {media_vendas}')

    menor_vendas = vendas[0]
    maior_vendas = vendas[0]
    for x in range(1, len(vendas)):
        if vendas[x] < menor_vendas:
            menor_vendas = vendas[x]
        if vendas[x] > maior_vendas:
            maior_vendas = vendas[x]

    comp = 0
    for x in vendas:
        if x == menor_vendas:
            print(f'O menor valor de vendas foi {menor_vendas} de {ilhas[comp]}')
        if x == maior_vendas:
            print(f'O maior valor de vendas foi {maior_vendas} de {ilhas[comp]}')
        comp += 1
