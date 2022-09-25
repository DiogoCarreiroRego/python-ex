"""
TPC

- Pede ao utilizador um número inicial.
- Pede ao utilizador um número que representa 'quantos'
- Monstrar aquela quantidade de primos a partir do número inicial
"""


def par(numero):
    return numero % 2 != 0


def primo(numero1, numero2):
    for x in range(numero1, numero2 + 1):
        if par(x):
            print(x)


if __name__ == '__main__':
    while True:
        num = int(input('Digite o número inicial: '))
        quantos = int(input('Quantos? '))
        quantos *= 2

        primo(num, quantos)

        continuar = input('Repetir [s | n]? ')
        if continuar == 'n':
            break
    print(f'Adeus!')