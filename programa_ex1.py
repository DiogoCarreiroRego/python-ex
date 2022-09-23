"""
Capítulo 2
Elementos Básicos de Programação
1º Exercício

- Vou pedir-lhe dois números
- Escreva o primeiro número, x = 5
- Escreva o segundo número, y = 6
- O valor de (x + 3 × y) × (x - y) = -23
"""


def valor(valor1, valor2):
    valor = (valor1 + 3 * valor2) * (valor1 - valor2)

    return valor


if __name__ == '__main__':
    nome = input('Como se chama? ')
    while True:
        x = int(input('Digite o primeiro número: '))
        y = int(input('Digite o segundo número: '))

        print(f'({x} + 3 × {y}) × ({x} - {y}) = {valor(x, y)}')

        continuar = input('Repetir (s | n)? ')
        if continuar == 'n':
            break
    print(f'Adeus {nome}!')