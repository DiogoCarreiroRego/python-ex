"""
Capítulo 2
Elementos Básicos de Programação
17º Exercício

- Dado um conjunto de n inteiros representando notas de alunos, escreva
um programa em Python para determinar quantos tiveram nota positiva.
Modifique o seu programa de modo a também calcular qual a percentagem
de notas positivas.
"""


if __name__ == '__main__':
    while True:
        try:
            nota_alunos = []
            num_alunos = int(input('Quantos alunos consiste na turma? '))

            num_alunos_positivo = 0
            perc_alunos_positivo = 0
            while num_alunos > 0:
                try:
                    num_alunos -= 1
                    nota_alunos.append(int(input('Digite a nota do aluno: ')))

                except ValueError:
                    num_alunos += 1
                    print('Digite um valor válido')

            print(nota_alunos)
            for x in range(len(nota_alunos)):
                if nota_alunos[x] >= 50:
                    num_alunos_positivo += 1

            print(f'Dos {len(nota_alunos)} alunos, apenas {num_alunos_positivo} tiraram positiva.')
            perc_alunos_positivo = (num_alunos_positivo * 100) / len(nota_alunos)
            print(f'Dos {len(nota_alunos)} alunos, apenas {int(perc_alunos_positivo)}% tiraram positiva.')

            continuar = input('Repetir (s | n)? ')
            if continuar == 'n':
                break

        except ValueError:
            print('Digite um valor válido')

    print(f'Adeus!')
