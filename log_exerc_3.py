"""
IMPORTANTE: Pythpm v 3.10
Exercicio 3 - Sistema para venda de feijoada
"""
# Funções
# Testa valor numérico
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


#Entrada de dados
while True:
    print('Bem-vindo ao Sistema de Venda de Feijoadas do Seu Zé!')
    x = float_teste(volume_feijoada())

    if x > 299 and x <= 5000:
        pass
    else:
        print('Não aceitamos porções menores do que 300mL nem maiores do que 5L!')
        break

    opt = ['B', 'P', 'S']
    lt = input('Entre com a opção desejada:\n'
               'B - (Feijão, paio e costelinha)\n'
               'P - (Feijão, paio, costelinha mais partes do porco)\n'
               'S - (Feijão, paio, costelinha, partes do porco, charque, calabresa, bacon)\n').upper()
    if lt in opt:
        val = calc_volume_feijoada(x) * op_feijoada(lt)
    else:
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
    op = ''
    while op != 0:
        op = input('Informe os acompanhamentos desejados: ')
        if op.isnumeric() and int(op) in op_list:
            op_list_calc.append(int(op))
            print('Deseja mais algum acompanhamento? ')
            op = int(op)
        else:
            print('Apenas números os valores informados!!!')

    print(f'O Valor a ser pago é R${val:.2f} (volume = {x} + R$ {op_feijoada(lt):.2f} opção + acompanhamento R$ {sum(op_list_calc):.2f})')

