"""
Capítulo 2
Elementos Básicos de Programação
20º Exercício

- Um programa que escreve o seguinte
    1 × 8 + 1 = 9
    12 × 8 + 2 = 98
    123 × 8 + 3 = 987
    1234 × 8 + 4 = 9876
    12345 × 8 + 5 = 98765
    123456 × 8 + 6 = 987654
    1234567 × 8 + 7 = 9876543
    12345678 × 8 + 8 = 98765432
    123456789 × 8 + 9 = 987654321
"""


def cal(valor1, valor2):
    produto = 8
    st = ''
    for x in range(valor1, valor2):
        st += str(x)
        cals = int(st) * produto + x
        print(f'{st} × {produto} + {x} = {cals}')


if __name__ == '__main__':
    while True:
        num_inicial = 1
        num_final = 10

        cal(num_inicial, num_final)

        continuar = input('Repetir (s | n)? ')
        if continuar == 'n':
            break
    print(f'Adeus!')
