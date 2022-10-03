"""
Capítulo 2
Elementos Básicos de Programação
15º Exercício

- Escreva um programa que lê uma série de dígitos (terminando com -1) e calcula o inteiro que tem esses dígitos.
Por exemplo, lendo os dígitos 1 5 4 5 8 -1, calcula o número inteiro 15458.
"""


if __name__ == '__main__':
    num_list = []
    while True:
        try:
            num = int(input('Digite um número: '))

            if num < 0:
                break

            num_list.append(num)

        except ValueError:
            print('Digite um valor válido')

    num = ''
    for x in range(len(num_list)):
        num += str(num_list[x])

    print(f'O número é: {num}')
    print(f'Adeus!')
