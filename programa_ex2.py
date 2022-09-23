"""
Capítulo 2
Elementos Básicos de Programação
2º Exercício

- Um programa que lê valores correspondentes a uma distância percorrida (em Km)
e o tempo necessário para percorrer (em minutos), e calcular a velocidade média em:
    (a) Km / h
    (b) m / s
* Calcular a velocidade média
"""


def media_km(valor1, valor2):
    valor2 = valor2 / 60
    media = valor1 / valor2

    return media


def media_m(valor1, valor2):
    valor1 = valor2 / 1000
    valor2 = valor2 * 60
    media = valor1 / valor2

    return media


if __name__ == '__main__':
    nome = input('Como se chama? ')
    while True:
        distancia = int(input('Qual foi a distância percorrida (em Km)? '))
        tempo = int(input('Qual é o tempo necessário a percorrer (em minutos)? '))

        print(f'{distancia}(Km) : {tempo}(min) = {media_km(distancia, tempo)} km/h')
        print(f'{distancia}(Km) : {tempo}(min) = {media_m(distancia, tempo)} m/s')

        continuar = input('Repetir (s | n)? ')
        if continuar == 'n':
            break
    print(f'Adeus {nome}!')
