"""
Capítulo 2
Elementos Básicos de Programação
14º Exercício

- Um programa que lê um inteiro e calcule a soma dos seus digitos.
"""


def digito(valor):
    # Contar o número de digitos
    #digitos = len(str(valor))

    # Soma de seus digitos
    valor = str(valor)
    digitos = 0
    for x in range(len(valor)):
        digitos += int(valor[x])

    return digitos


if __name__ == '__main__':
    while True:
        try:
            num = int(input('Qual é o número? '))

            print(f'O número {num} contém {digito(num)} em soma de seus digitos.')

            continuar = input('Repetir (s | n)? ')
            if continuar == 'n':
                break

        except ValueError:
            print('Digite um valor válido')

    print(f'Adeus!')
