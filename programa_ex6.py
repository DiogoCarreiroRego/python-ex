"""
Capítulo 2
Elementos Básicos de Programação
6º Exercício

- Um programa que lê três números e que diz qual o maior dos números lidos.
"""


def larger(valor1, valor2, valor3):
    maior = 0
    if num1 > num2 and num1 > num3:
        maior = num1
    elif num2 > num1 and num2 > num3:
        maior = num2
    elif num3 > num1 and num3 > num2:
        maior = num3

    return maior


if __name__ == '__main__':
    while True:
        try:
            num1 = int(input('Qual é o primeiro número? '))
            num2 = int(input('Qual é o segundo número? '))
            num3 = int(input('Qual é o terceiro número? '))

            print(f'O maior número é {larger(num1, num2,num3)}.')

            continuar = input('Repetir (s | n)? ')
            if continuar == 'n':
                break

        except ValueError:
            print('Digite um valor válido')

    print(f'Adeus!')
