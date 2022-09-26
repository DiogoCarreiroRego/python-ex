"""
Capítulo 2
Elementos Básicos de Programação
18º Exercício

- Escreve um programa que lê um número inteiro e detemina quantas vezes aparecem dois
zeros seguintes. Por exemplo:

"""
# https://pt.stackoverflow.com/questions/112972/como-contar-os-zeros-%C3%A0-direita-de-um-n%C3%BAmero


def countZeros(numero):
    count = 0;
    while numero % 10 == 0:
        count += 1
        numero /= 10
    return count


if __name__ == '__main__':
    while True:
        num = int(input('Digite o número inicial: '))

        print(f'O número {num} tem {countZeros(num)} zeros.')

        continuar = input('Repetir [s | n]? ')
        if continuar == 'n':
            break
    print(f'Adeus!')