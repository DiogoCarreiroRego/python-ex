"""
TPC

- Pede dois números ao utilizador.
    * O segundo número deve ser maior ou igual ao primeiro númerio
    * Monstrar todos os números primos que há entre o primeiro e segundo número
    * Depois de monstrar os números primos, dizer quantos primos havia
"""


def par(numero):
    return numero % 2 != 0


def primo(numero1, numero2):
    primos = 0
    for x in range(numero1, numero2 + 1):
        if par(x):
            primos += 1
            print(x)

    return primos


if __name__ == '__main__':
    while True:
        num1 = int(input('Digite o primeiro número: '))
        num2 = 0
        while num2 < num1:
            num2 = int(input('Digite o segundo número: '))
            if num2 < num1:
                print('O segundo número deve ser maior que o primeiro.')

        print(f'Tem {primo(num1, num2)}')

        continuar = input('Repetir [s | n]? ')
        if continuar == 'n':
            break
    print(f'Adeus!')