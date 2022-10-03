"""
Capítulo 2
Elementos Básicos de Programação
9º Exercício

- Um programa que lê uma sequência de dígitos, sendo cada um dos
dígitos fornecido numa linha separada, e calcula o número inteiro
composto por esses dígitos, pela ordem fornecida. Para terminar a
sequência de dígitos é fornecido ao programa o inteiro 1.
O seu programa deve permitir a interação:
Escreva um dígito
(-1 para terminar)
? 3
Escreva um dígito
(-1 para terminar)
? 2
Escreva um dígito
(-1 para terminar)
? 5
Escreva um dígito
(-1 para terminar)
? 7
Escreva um dígito
(-1 para terminar)
? -1
O número é: 3257
"""


if __name__ == '__main__':
    num_list = []
    while True:
        try:
            num = int(input('Digite um número: '))

            if num < 0:
                break

            num_list.append(num)

        except ValueError:
            print('Digite um valor válido')

    num = ''
    for x in range(len(num_list)):
        num += str(num_list[x])

    print(f'O número é: {num}')
    print(f'Adeus!')
