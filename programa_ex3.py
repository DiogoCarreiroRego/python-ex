"""
Capítulo 2
Elementos Básicos de Programação
3º Exercício

- Um programa que pede ao utilizador que lhe forneça um inteiro correspondente a
um número de segundos e que calcula o número de dias correspondentes a esse número
de segundos.
    * Escreve um número de segundos
    * Exemplo - 65432998
    * O número de dias correspondentes é 757.3263657407407
"""


def calculo(valor):
    """
    segundos = 86400
    minutos = segundos / 60
    horas = minutos / 60
    dias = horas / 24
    """
    # Cada 1 minuto equivale a 60 segundos
    valor = valor / 60
    # Cada 1 hora equivale a 60 minutos
    valor = valor / 60
    # Cada 1 dia evivale a 24 horas
    valor = valor / 24

    return valor


if __name__ == '__main__':
    nome = input('Como se chama? ')
    while True:
        segundos = int(input('Quantos segundos? '))

        print(f'{nome}, os {segundos} segundos equivalem a {calculo(segundos)} dias.')

        continuar = input('Repetir (s | n)? ')
        if continuar == 'n':
            break
    print(f'Adeus {nome}!')
