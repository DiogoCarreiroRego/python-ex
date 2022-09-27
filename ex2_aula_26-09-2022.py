"""
Peça ao utilizador para inserir uma frase
Após o utilizador ter inderido a frase apresente:
 - Qual é o comprimento da frase inserida (incluindo espaços)
 - Quantas palavras tem a frase
 - Quantas vogais tem a frase
 - Quantas letras maiusculas tem a frase
 - Quantas letras minusculas tem a frase
 - Quantos numeros tem a frase
 - Apresente a frase invertida. Exemplo: A frase é 'Bom dia!' deve dar '!aid moB'
"""


if __name__ == '__main__':
    frase_list = []
    frase = str(input('Digite uma frase: '))
    frase_list.append(frase)

    num_palavras = len(frase.split(' '))
    num_mai = 0
    num_min = 0
    num_vogais = 0
    num_numbers = 0
    for x in range(len(frase)):
        if frase[x].islower():
            num_min += 1
        elif frase[x].isupper():
            num_mai += 1
        elif frase[x].isdigit():
            num_numbers += 1
        if frase[x] == 'a' or frase[x] == 'e' or frase[x] == 'i' or frase[x] == 'o' or frase[x] == 'u' or frase[x] == 'A' or frase[x] == 'E' or frase[x] == 'I' or frase[x] == 'O' or frase[x] == 'U':
            num_vogais += 1

    num_letras = (num_mai + num_min)
    num_consoantes = num_letras - num_vogais

    print(f'A é frase escrita foi "{frase_list}"')
    print(f'A frase contém {num_palavras} palavras')
    print(f'A frase contém {num_letras} letras')
    print(f'A frase contém {num_vogais} vogais')
    print(f'A frase contém {num_consoantes} consoantes')
    print(f'A frase contém {num_numbers} números')
    print(f'A frase contém {num_mai} letras maiusculas')
    print(f'A frase contém {num_min} letras minusculas')
    reversed_frase = ''
    for i in reversed(frase):
        reversed_frase += i
    print(f'A é frase escrita quanto invertida fica "{reversed_frase}"')
    print(f'A é frase escrita quanto invertida fica "{frase[::-1]}"')