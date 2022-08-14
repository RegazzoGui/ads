"""
IMPORTANTE - Python versão 3.10
Exercício 1 - Sistema para PedShop
"""
#Funções
    #Aliquota de desconto
def descontos(qtde):
    if qtde < 4:
        desc = 0.00
    elif qtde > 4 and qtde <= 19:
        desc = 0.03
    elif qtde >= 20 and qtde <= 99:
        desc = 0.06
    else:
        desc = 0.1
    return desc


#Teste numérico
def is_number(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

#Inicio
msg = 'Autopeças Novo mundo'
print('==' * 20)
print(msg.center(40))
print('==' * 20)

val_prod = input('Entre com o valor do produto: ')
while not is_number(val_prod):
    print('\tApenas valores numéricos são permitidos!')
    val_prod = input('\tEntre com o valor do produto: ')

qtde = input('Entre com a quantidade de produtos: ')
while not is_number(qtde):
    print('\tApenas valores numéricos são permitidos!')
    qtde = input('\tEntre com o valor do produto: ')


#Total
val_prod = float(val_prod)
qtde = int(val_prod)
aliq = descontos(qtde)

total = val_prod * qtde
total_desc = total - (total * aliq)

print(f'O valor sem desconto foi: R${total:.2f}')
print(f'O valor com desconto foi: R${total_desc:.2f}  (desconto de {(aliq * 100):.1f}%)')
