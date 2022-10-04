"""
Capítulo 2
Elementos Básicos de Programação
12º Exercício

- Um programa que calcula o valor da soma.
"""


if __name__ == '__main__':
    while True:
        try:
            x = int(input('Qual o valor de x: '))
            n = int(input('Qual o valor de n: '))

            soma = 1 + x
            for z in range(2, n + 1):
                soma += (x ** z) / z

            print(soma)

            continuar = input('Repetir (s | n)? ')
            if continuar == 'n':
                break

        except ValueError:
            print('Digite um valor válido')

    print(f'Adeus!')
