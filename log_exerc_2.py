"""
IMPORTANTE: Python v 3.10
"""
#Listas contendo informações pertinentes
cod = [21, 22, 23, 24, 25]
desc = ['Napolitana', 'Margherita', 'Calabresa', 'Toscana', 'Portuguesa']
val_pm = [20, 20, 25, 30, 30]
val_pg = [26, 26, 32, 39, 39]


#Inicio Main
#reproduzindo o quadro de informações
msg = 'Cardápio'
msg_1 = 'Pizzaria do Aluisio G S Regazzo'
print(msg_1.center(65))
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

#Entrada de dados: sabor e tamanho
#Entrada tamanho da pizza
while rep != 0:
    t = ['M', 'G']
    tam = input('Qual o tamanho da pizza que deseja (M/G): ').upper()
    while True:
        try:
            if tam in t:
                break
            else:
                print('OPÇÃO INVÁLIDO - Por favor, digite apenas "M" ou "G"')
                tam = input('Qual o tamanho da pizza que deseja (M/G): ').upper()
        except ValueError:
            break


#Entrada nome da pizza

    c_list = [21, 22, 23, 24, 25]
    c = int(input('Entre com o código do sabor desejado: '))
    while True:
        try:
            if c in c_list:
                break
            else:
                print('OPÇÃO INVÁLIDO - Digite apenas os códigos presentes no cardápio!')
                c = int(input('Entre com o código do sabor desejado: '))
        except ValueError:
            break

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

    rep = int(input('Deseja pedir mais alguma coisa?\n'
          '1 - Sim\n'
          '0 - Não\n'
          '>>> '))

    tot.append(preco)


total = float(sum(tot))
print(f'O total a ser pago é: R$ {total:.2f}')
