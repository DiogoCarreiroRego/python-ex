"""
Complete o programa

Pergunte ao utilizador quantos números quer
Pergunte ao utilizador qual é o intervalo para obter numeros aleatórios
Pergunte se deseja ver apenas pares, apenas impares ou apenas primos
Mostre todos os números aleatórios
Mostre todos os números que satisfazem o pedido do utilizador
"""
import random


def divisores(num):
    zeros = 0
    for nn in range(1, num + 1):
        if num % nn == 0:
            zeros += 1  # zeros = zeros + 1
    return zeros


def get_random(ini, fim):
    """
    Esta função devolve um número aleatório entre ini e fim inclusive
    :param ini: inicío do intervalo
    :param fim: fim do intervalo
    :return: número aleatório
    """
    return random.randrange(ini, fim + 1)


if __name__ == '__main__':
    while True:
        try:
            quantos = int(input('Quantos? '))
            break
        except ValueError:
            print('Insere valores válidos!')

    while True:
        try:
            ini = int(input('Valor inicial? '))
            fim = int(input('Valor final? '))
            if fim < ini:
                print("O valor final não pode ser menor que o inicial")
                continue
            break
        except:
            print('Insere valores válidos')

    for num in range(quantos):
        numero = get_random(ini, fim)
        print(numero)
        if numero % 2 == 0:
            out1 = f'O numero {numero} é par'
        else:
            out1 = f'O numero {numero} é impar'
        if divisores(numero)  == 2:
            out2 = 'e primo'
        else:
            out2 = ''
        print(f'{out1} {out2}')