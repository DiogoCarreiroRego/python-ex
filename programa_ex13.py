"""
Capítulo 2
Elementos Básicos de Programação
13º Exercício

- Um programa que pede ao utilizador que forneça um número e que escreve a tabuada da
multiplicação que este número.
- O seu programa deve gerar uma interação como o seguinte:
"""


def cal(valor):
    for x in range(1, 11):
        mult = valor * x
        print(f'{valor} × {x} = {mult}')


if __name__ == '__main__':
    while True:
        num = int(input('Qual é o número? '))

        cal(num)

        continuar = input('Repetir (s | n)? ')
        if continuar == 'n':
            break
    print(f'Adeus!')
