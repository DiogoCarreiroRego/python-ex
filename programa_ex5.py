"""
Capítulo 2
Elementos Básicos de Programação
5º Exercício

- Um programa que lê cinco números reais e calcula a sua média e o
seu desvio padrão.
A média, X, e o desvio padrão, a, de cinco números x1, ... x5.
"""

from math import sqrt


if __name__ == '__main__':
    while True:
        try:
            num_ini = int(input('Digite o número inicial: '))
            num_end = int(input('Digite o número final: '))
            X = []  # Lista de mádias de x
            a = []  # Lista de desvio padrão em a

            for Z in range(num_ini, num_end + 1):
                X.append(Z / 5)

            for Z in range(num_ini, num_end + 1):
                a.append(sqrt((1 / 4) * (Z - X[Z - 1]) ** 2))

            print(f'A média é {X}')
            print(f'O desvio padrão {a}')

            continuar = input('Repetir (s | n)? ')
            if continuar == 'n':
                break

        except ValueError:
            print('Digite um valor válido')
