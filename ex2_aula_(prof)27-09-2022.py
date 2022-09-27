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
    vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    frase = input('Insere uma frase: ')
    x = 0
    for c in frase:
        x += 1

    print(f'A frase tem {x} caracters = {len(frase)}')

    num_vogais = 0
    for c in frase:
        if c in vogais:
            num_vogais += 1
    print(f'A frase tem {num_vogais} vogais.')

    novafrase = frase.split(' ')
    print(novafrase)
    print(len(novafrase))

    maiusculas = 0
    minusculas = 0
    for c in frase:
        if c != ' ':
            if c == c.upper():
                maiusculas += 1
            if c == c.lower():
                minusculas += 1
    print(f'A frase tem {minusculas} minusculas e {maiusculas} maisculas.')

    osnums = 0
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for c in frase:
        if c in nums:
            osnums += 1
    print(f'Tem {osnums} numeros')

    osnums = 0
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for c in frase:
        try:
            if int(c) in nums:
                osnums += 1
        except:
            pass
    print(f'v2Tem {osnums} numeros')


    invertido = []
    for c in frase:
        invertido.append(c)

    nova = invertido

    qtd = len(invertido) - 1

    for c in frase:
        nova[qtd] = c
        qtd -= 1

    print(f'nova = {nova}')
    print(f"nova = {''.join(nova)}")



    print(f'frase = {frase}')
    print(f'invertido = {invertido}')







"""
    continuar = 's'
    while continuar == 's':
        ini = int(input('Insira o número inicial '))
        fim = int(input('Insira o número final '))
        primos = 0
        for n in range(ini, fim + 1):
            if divisores(n) == 2:
                primos += 1
        print(f'Entre {ini} e {fim} há {primos} de primos.')
        continuar = input('Repetir [s | n]? ')
    print(f'Adeus!')
"""