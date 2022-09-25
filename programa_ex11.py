"""
Capítulo 2
Elementos Básicos de Programação
11º Exercício

- Um programa que lê um número inteiro positivo e produz o número correspondente
a inverter a ordem dos seus digitos. Por exemplo:
    * Escreve um inteiro positivo
    ? 7633256
    * O número invertido é  6523367
"""


def numero(valor):
    valor = str(valor)
    numero = valor[::-1]

    return numero


if __name__ == '__main__':
    while True:
        num = int(input('Qual é o número? '))

        print(f'O número invertido é {numero(num)}.')

        continuar = input('Repetir (s | n)? ')
        if continuar == 'n':
            break
    print(f'Adeus!')
