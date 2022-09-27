"""
Peça ao utilizador para inserir uma frase
Após o utilizador ter inderido a frase apresente:
 - Imprima a frase, mas com cada palavra invertida. Por exemplo 'Bom dia!' deve dar 'moB !aid'
 - Imprima a frase, mas com as maiusculas em minisculo e as minusculas em maiusculas.

 - Quantas palavras tem a frase
 - Quantas vogais tem a frase
 - Quantas letras maiusculas tem a frase
 - Quantas letras minusculas tem a frase
 - Quantos numeros tem a frase
 - Apresente a frase invertida. Exemplo: A frase é 'Bom dia!' deve dar '!aid moB'
"""


if __name__ == '__main__':
    vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    phrase = input(f'Digite uma frase: ')

    num_words = len(phrase.split(' '))

    num_maiusculas = 0
    num_minusculas = 0
    for x in range(len(phrase)):
        if phrase[x].islower():
            num_minusculas += 1
        elif phrase[x].isupper():
            num_maiusculas += 1

    num_letters = num_maiusculas + num_minusculas

    num_numbers = 0
    num_vogais = 0
    for x in phrase:
        if x in vogais:
            num_vogais += 1
        if x in nums:
            num_numbers += 1

    num_consoantes = num_letters - num_vogais

    phrase_reversed = phrase[::-1]
    words_reversed = ''
    for x in phrase.split():
        words_reversed += x[::-1] + ' '

    reversed_letters = ''
    for x in phrase:
        if x == x.lower():
            x = x.upper()
        elif x == x.upper():
            x = x.lower()
        reversed_letters += x

    print(f'A frase escrita quanto a palavras invertidas fica {words_reversed}')
    print(f'A frase escrita quanto a letras maiusculas e minisculo invertidas fica {reversed_letters}')
    print(f'A frase contém {num_words} palavras')
    print(f'A frase contém {num_letters} letras')
    print(f'A frase contém {num_maiusculas} letras maisculas')
    print(f'A frase contém {num_minusculas} letras minusculas')
    print(f'A frase contém {num_numbers} números')
    print(f'A frase contém {num_vogais} vogais')
    print(f'A frase contém {num_consoantes} consoantes')
    print(f'A frase escrita quanto invertida fica "{phrase_reversed}"')
