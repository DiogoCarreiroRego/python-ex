"""
Capítulo 2
Elementos Básicos de Programação
8º Exercício

- Um programa que pede ao utilizador que lhe forneça uma secessão de inteiros correspondentes a
valores em segundos e que calcula o número de dias correspondentes a cada um desses inteiros.
- O programa termina quando o utilizador fornece um número negativo.
- O seu programa deve possibilitar a seguinte interação:
    * Escreve um número de segundos
    (um número negativo para terminar)
    ? 45
    * O número de dias correspondente é 0.000520833333...
    * Escreve um número de segundos
    (um número negativo para terminar)
    ? -1
"""


def dia(valor):
    dias = valor / (24 * 3600)

    return dias


if __name__ == '__main__':
    while True:
        segundos = int(input('Quantas segundos? '))

        print(f'{segundos} segundos correspondem a {dia(segundos)} dias.')

        if segundos < 0:
            break
    print(f'Adeus!')
