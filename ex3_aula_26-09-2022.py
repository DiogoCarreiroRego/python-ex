"""
Complete o programa

# Perguntar ao utilizador quantos números quer
Pergunte ao utilizador qual é o intervalo para obter numeros aleatórios
Pergunte se deseja ver apenas pares, apenas impares ou apenas primos
Mostre todos os números aleatórios
Mostre todos os números que satisfazem o pedido do utilizador
"""
import random


def get_random(ini, fim):
    """
    Esta função devolve um número aleatório entre ini e fim inclusive
    :param ini: inicío do intervalo
    :param fim: fim do intervalo
    :return: número aleatório
    """

    return random.randrange(ini, fim + 1)


def par(num):
  return num % 2 == 0


def impar(num):
  return num % 2 != 0


if __name__ == '__main__':
  num_ini = int(input(f'Qual é o número inicial? '))
  num_end = int(input(f'Qual é o número final? '))
  opcao = int(input(f'Qual opção deseja [par - 1, impar - 2, primo - 3]? '))

  num_random = 0
  list_random = []
  list_random_par = []
  list_random_impar = []
  list_random_primo = []

  for x in range(num_ini, num_end + 1):
    num_random = get_random(num_ini, num_end)

    list_random.insert(x, num_random)

    if opcao == 1:
      if par(num_random):
        list_random_par.insert(x, num_random)

    elif opcao == 2:
      if impar(num_random):
        list_random_impar.insert(x, num_random)

    elif opcao == 3:
      # A parte dos números primos não está correta
      if impar(num_random):
        list_random_primo.insert(x, num_random)

  print(f'Lista {list_random}')

  if opcao == 1:
    print(f'Lista Par {list_random_par}')
  elif opcao == 2:
    print(f'Lista Impar {list_random_impar}')
  elif opcao == 3:
    print(f'Lista Primos {list_random_primo}')