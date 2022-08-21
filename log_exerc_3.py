"""
IMPORTANTE: Pythpm v 3.10
Exercicio 3 - Sistema para venda de feijoada
"""
# Funções
def float_teste(vol):
    try:
        float(vol)
        return float(vol)
    except ValueError:
        print('Apenas números são permitidos!')
        return False


# Calcula o preço da feijoada
def calc_volume_feijoada(vol):
    return vol * 0.08


def volume_feijoada():
    vol = input('Informe o volume desejado (mL): ')
    return vol


def op_feijoada(let):
    match let:
        case 'B':
            return 1
        case 'P':
            return 1.25
        case 'S':
            return 1.5


def op_acompanhamento(num):
    match num:
        case 1:
            return 5
        case 2:
            return 6
        case 3:
            return 7
        case 4:
            return 3

#Inicio da Main
#Entrada de dados
print('Bem-vindo ao Sistema de Venda de Feijoadas - Aluisio G S Regazzo')
x = float_teste(volume_feijoada())
while True:
    try:
        if x >= 300 and x <= 5000:
            break
        else:
            print('Não aceitamos porções menores do que 300mL nem maiores do que 5L!')
            x = float_teste(volume_feijoada())
    except ValueError:
        break

opt = ['B', 'P', 'S']
lt = input('Entre com a opção desejada:\n'
           'B - (Feijão, paio e costelinha)\n'
           'P - (Feijão, paio, costelinha mais partes do porco)\n'
           'S - (Feijão, paio, costelinha, partes do porco, charque, calabresa, bacon)\n'
           '>>> ').upper()
while True:
    try:
        if lt in opt:
            val = calc_volume_feijoada(x) * op_feijoada(lt)
            break
        else:
            lt = input('OPÇÃO INVÁLIDA - Entre com a opção desejada:\n'
                       'B - (Feijão, paio e costelinha)\n'
                       'P - (Feijão, paio, costelinha mais partes do porco)\n'
                       'S - (Feijão, paio, costelinha, partes do porco, charque, calabresa, bacon)\n'
                       '>>> ').upper()
    except ValueError:
        break

print('Escolha o acompanhamento:\n'
      '                     Rota                                   Valor\n'
      '0 - Não desejo acompanhamento, encerrar o pedido.\n'
      '1 - 200g de arros                 ---------------          R$ 5,00\n'
      '2 - 150g de farofa especial       ---------------          R$ 6,00\n'
      '3 - 100g de couve cozida          ---------------          R$ 7,00\n'
      '4 - 1 laranja descascada          ---------------          R$ 3,00')

op_list = [0, 1, 2, 3, 4]
op_list_calc = []
op = input('Informe os acompanhamentos desejados: ')
while op != 0:
    try:
        if int(op) in op_list:
            op_list_calc.append(int(op))
            op = int(input('Deseja mais algum acompanhamento?\n'
                   '>>> '))
        else:
            print('OPÇÃO INVÁLIDA - Apenas os produtos informados!!!')
            op = int(input('Deseja mais algum acompanhamento?\n'
                           '>>> '))
    except ValueError:
        break


print(f'O Valor a ser pago é R${val:.2f} (volume = {x:.2f}mL + R$ {op_feijoada(lt):.2f} opção + acompanhamento R$ {sum(op_list_calc):.2f})\n'
      f'Obrigado!\n')

#Final da main
