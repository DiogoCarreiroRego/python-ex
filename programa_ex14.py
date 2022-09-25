"""
Capítulo 2
Elementos Básicos de Programação
14º Exercício

- Um programa que lê um inteiro e calcule a soma dos seus digitos.
"""


def digito(valor):
    digitos = len(str(valor))

    return digitos

if __name__ == '__main__':
    while True:
        num = int(input('Qual é o número? '))

        print(f'O número {num} contém {digito(num)} digitos.')

        continuar = input('Repetir (s | n)? ')
        if continuar == 'n':
            break
    print(f'Adeus!')
