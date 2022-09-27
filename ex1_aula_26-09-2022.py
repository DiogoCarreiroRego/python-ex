"""
Declare uma lista para guardar as vendas do grupo central
Declara uma lista para guardar os nomes das cinco ilhas do grupo central
Peça dados ao utilizador e guarde-os na lista
Após o utilizador ter inserido os 5 valores apresente:
- Total das vendas
- O menor valor inserido
- O maior valor inserido
- A média das vendas.
"""


if __name__ == '__main__':
  vendas_grupo_central = []
  nome_ilhas_grupo_central = []
  valores = 5

  for x in range(0, valores):
    num_vendas = int(input(f'Qual é o {x + 1}º número de vendas? '))
    nome_ilha = str(input(f'Qual é a ilha do grupo central? '))

    vendas_grupo_central.insert(x, num_vendas)
    nome_ilhas_grupo_central.insert(x, nome_ilha)

  print(f'\nVendas - {vendas_grupo_central}')
  print(f'Ilhas - {nome_ilhas_grupo_central}')
  print(f'Total de vendas é {sum(vendas_grupo_central)}')
  print(f'Menor vendas foi {min(vendas_grupo_central)}')
  print(f'Maior vendas foi {max(vendas_grupo_central)}')
  print(f'Média de vendas foi {sum(vendas_grupo_central) / len(vendas_grupo_central)}')

