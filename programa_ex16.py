"""
Capítulo 2
Elementos Básicos de Programação
16º Exercício

- Um programa que lê um número e crie a uma capicua cuja primeira metade é o número lido.
Por exemplo:
    * Escreve um número
    ? 347
    347743
"""


def numero(valor):
    valor = str(valor)
    numero = valor + valor[::-1]

    return numero


if __name__ == '__main__':
    while True:
        try:
            num = int(input('Qual é o número? '))

            print(f'O número é {numero(num)}.')

            continuar = input('Repetir (s | n)? ')
            if continuar == 'n':
                break

        except ValueError:
            print('Digite uma valor válido')

    print(f'Adeus!')
