"""
Capítulo 2
Elementos Básicos de Programação
7º Exercício

- Um programa que lê o número de horas, que um empregado trabalhou numa dada semana e os eu
salário/hora e calcula o ordenado semanal tendo em conta as horas extraordinárias.
- O salário é calculado do seguinte modo: se o número de horas for menor que 40 então salário é
dado plo produto do número de horas pelo salário/hora, em caso contrário recebe horas
extraordinárias as quais são pagas a dobrar.
"""


def salario(valor1, valor2):
    if hora_semanal > 40:
        valor2 *= 2

    salario_semanal = valor1 * valor2

    return salario_semanal


if __name__ == '__main__':
    while True:
        try:
            hora_semanal = int(input('Quantas horas trabalhou esta semana? '))
            salario_hora = int(input('Qual é o seu salário por hora? '))

            print(f'O seu salário é {salario(hora_semanal, salario_hora)}€.')

            continuar = input('Repetir (s | n)? ')
            if continuar == 'n':
                break

        except ValueError:
            print('Digite um valor válido')

    print(f'Adeus!')
