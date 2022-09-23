"""
Capítulo 2
Elementos Básicos de Programação
4º Exercício

- Um programa que lê um número inteiro correspondente a um certo número de segundos e que escreve
o número de dias, horas, minutos, segundos correspondentes a esse número. Por exemplo:
    * Escreve o número de segundos 345678
    * dias : 4 horas: 0 mins: 1 segs: 18
"""


def dia(valor):
    dias = valor / 60
    dias = dias / 60
    dias = dias / 24

    return dias


def hour(valor):
    hours = valor % (24 * 3600)
    hours = hours // 3600

    return hours


def min(valor):
    mins = valor % (24 * 60)
    mins = mins // 60

    return mins


def seg(valor):
    segs = valor
    segs %= 60

    return segs


if __name__ == '__main__':
    while True:
        segundos = int(input('Quantos segundos? '))

        print(f'dias: {int(dia(segundos))} mins: {int(hour(segundos))} mins: {int(min(segundos))} segs: {int(seg(segundos))}')

        continuar = input('Repetir (s | n)? ')
        if continuar == 'n':
            break
    print(f'Adeus!')
