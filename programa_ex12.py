"""
Capítulo 2
Elementos Básicos de Programação
10º Exercício

- Um programa que
"""


if __name__ == '__main__':
    while True:
        try:
            x = int(input('Qual o valor de x: '))
            n = int(input('Qual o valor de n: '))


            continuar = input('Repetir (s | n)? ')
            if continuar == 'n':
                break

        except ValueError:
            print('Digite um valor válido')

    print(f'Adeus!')
