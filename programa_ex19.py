"""
Capítulo 2
Elementos Básicos de Programação
19º Exercício

- Um programa que lê uma quantidade em Euros e calcula o número de nota de 50€ a 5€ e
moedas de 2€ a 1€ e cêncimos de 0.5€ a 0.01€
"""


def nota(valor):
    valor = float(valor)
    notas_50 = int(valor // 50)
    notas_20 = int((valor - (notas_50 * 50)) // 20)
    notas_10 = int((valor - (notas_50 * 50) - (notas_20 * 20)) // 10)
    moedas_5 = int((valor - (notas_50 * 50) - (notas_20 * 20) - (notas_10 * 10)) // 5)
    moedas_2 = int((valor - (notas_50 * 50) - (notas_20 * 20) - (notas_10 * 10) - (moedas_5 * 5)) // 2)
    moedas_1 = int((valor - (notas_50 * 50) - (notas_20 * 20) - (notas_10 * 10) - (moedas_5 * 5) - (moedas_2 * 2)) // 1)
    centimos__50 = int((valor - (notas_50 * 50) - (notas_20 * 20) - (notas_10 * 10) - (moedas_5 * 5) - (moedas_2 * 2) - (moedas_1 * 1)) // 0.5)
    centimos__20 = int((valor - (notas_50 * 50) - (notas_20 * 20) - (notas_10 * 10) - (moedas_5 * 5) - (moedas_2 * 2) - (moedas_1 * 1) - (centimos__50 * 0.5)) // 0.2)
    centimos__10 = int((valor - (notas_50 * 50) - (notas_20 * 20) - (notas_10 * 10) - (moedas_5 * 5) - (moedas_2 * 2) - (moedas_1 * 1) - (centimos__50 * 0.5) - (centimos__20 * 0.2)) // 0.1)
    centimos__5 = int((valor - (notas_50 * 50) - (notas_20 * 20) - (notas_10 * 10) - (moedas_5 * 5) - (moedas_2 * 2) - (moedas_1 * 1) - (centimos__50 * 0.5) - (centimos__20 * 0.2) - (centimos__10 * 0.1)) // 0.05)
    centimos__2 = int((valor - (notas_50 * 50) - (notas_20 * 20) - (notas_10 * 10) - (moedas_5 * 5) - (moedas_2 * 2) - (moedas_1 * 1) - (centimos__50 * 0.5) - (centimos__20 * 0.2) - (centimos__10 * 0.1) - (centimos__5 * 0.05)) // 0.02)
    centimos__1 = int((valor - (notas_50 * 50) - (notas_20 * 20) - (notas_10 * 10) - (moedas_5 * 5) - (moedas_2 * 2) - (moedas_1 * 1) - (centimos__50 * 0.5) - (centimos__20 * 0.2) - (centimos__10 * 0.1) - (centimos__5 * 0.05) - (centimos__2 * 0.02)) // 0.01)
    print(f'[{notas_50}]50€ [{notas_20}]20€ [{notas_10}]10€ [{moedas_5}]5€ [{moedas_2}]2€ [{moedas_1}]1€')
    print(f'[{centimos__50}]0.5€ [{centimos__20}]0.2€ [{centimos__10}]0.1€ [{centimos__5}]0.05€ [{centimos__2}]0.02€ [{centimos__1}]0.01€')


if __name__ == '__main__':
    while True:
        euro = input('Qual é a quantidade em euros? ')

        nota(euro)

        continuar = input('Repetir (s | n)? ')
        if continuar == 'n':
            break
    print(f'Adeus!')
