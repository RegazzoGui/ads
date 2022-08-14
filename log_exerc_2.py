"""
IMPORTANTE: Python v 3.10
Exericio 2 - Sistema para Pizzaria
"""
#Criando a tabela com os dados
cod = [21, 22, 23, 24, 25]
desc = ['Napolitana', 'Margherita', 'Calabresa', 'Toscana', 'Portuguesa']
val_pm = [20, 20, 25, 30, 30]
val_pg = [26, 26, 32, 39, 39]

#reproduzindo o quadro de informações
msg = 'Cardápio'
print(msg.center(65, '-'))
print('|  Código   |   Descrição   |   Pizza Média   |   Pizza Grande  |\n'
      '-----------------------------------------------------------------\n'
      '|    21     |   Napolitana  |     R$ 20,00    |   R$ 26,00      |\n'
      '|    22     |   Margherita  |     R$ 20,00    |   R$ 26,00      |\n'
      '|    23     |   Calabresa   |     R$ 25,00    |   R$ 32,00      |\n'
      '|    24     |   Toscana     |     R$ 30,00    |   R$ 39,00      |\n'
      '|    25     |   Portuguesa  |     R$ 30,00    |   R$ 39,00      |')
print('-' * 65)

#Estrutura de repetição
tot = []
rep = ''
while rep != 0:
    #Entrada de dados, sabor e tamanho
    #Entrada tamanho da pizza
    t = ['M', 'G']
    tam = input('Qual o tamanho da pizza que deseja (M/G): ').upper()
    if tam not in t:
        print('TAMANHO INVÁLIDO - Por favor, digite apenas "M" ou "G"')
        tam = input('Qual o tamanho da pizza que deseja (M/G): ').upper()


    #Entrada nome da pizza
    c_list = [21, 22, 23, 24, 25]
    c = int(input('Entre com o código do sabor desejado: '))
    if c not in c_list:
        print('CÓDIGO INVÁLIDO - Digite apenas os códigos presentes no cardápio!')
        c = input('Entre com o código do sabor desejado: ')

    # Indicando o sabor e o preço
    #Escolha do sabor
    sabor = ''
    nome_pizza = dict(zip(cod, desc))
    for k, v in nome_pizza.items():
       if k == c:
           sabor = v

    #Escolha do tamanho/preco da pizza
    if tam == 'M':
        valor = dict(zip(cod, val_pm))
    else:
        valor = dict(zip(cod, val_pg))

    for k_vp, v_vp in valor.items():
        if k_vp == c:
            preco = v_vp

    print(f'Você pediu a pizza de {sabor}')

    print('Deseja pedir mais alguma coisa?\n'
          '1 - Sim\n'
          '0 - Não')
    rep = int(input())

    tot.append(preco)

total = float(sum(tot))
print(f'O total a ser pago é: R$ {total:.2f}')
