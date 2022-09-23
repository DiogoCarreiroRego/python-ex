"""
Este programa implementa funções aritméticas
"""


def aritmetica(valor1, valor2, op='+'):
    """
    Esta função implementa as operações de somar, subtrair, multiplicar e dividir
    :param valor1: Primeiro fator da operação
    :param valor2: Segundo fator da operação
    :param op: Operação; valores válidos são; + - : *
    :return: Resultado da operação
    """
    total = 'Código de operação inválido'
    if op == '+':
        total = valor1 + valor2
    if op == '-':
        total = valor1 - valor2
    if op == ':':
        total = valor1 / valor2
    if op == '*':
        total = valor1 * valor2

    return total


if __name__ == '__main__':
    nome = input('Como te chamas? ')
    continuar = 's'
    while continuar == 's':
        fator1 = float(input('Insira o primeiro número '))
        fator2 = float(input('Insira o segundo número '))
        operacao = input('Insira a operação [+ , -, :, *] ')
        print(f'Olá {nome}, {fator1} {operacao} {fator2} = {aritmetica(fator1, fator2, operacao)}')
        continuar = input('Repetir [s | n]? ')
    print(f'Adeus {nome}!')