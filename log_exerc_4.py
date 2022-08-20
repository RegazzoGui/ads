"""
IMPORTANTE = Python v 3.10
EXERCICIO 4
"""
from time import sleep
#Lista
lista_produtos = []

# Funções
# Cadastrar Produto
def cadastrar_produtos(cod):
    print("Bem-vindo ao CADASTRO de Produtos")
    print(f'O código do produto a ser cadastrado é {cod}')
    prod = input('Informe o nome do produto: ')
    fab = input('Informe o fabricante do produto: ')
    prec = float(input('Informe o valor do produto: '))
    prod_dict = {
        'cod'  : cod,
        'prod' : prod,
        'fab'  : fab,
        'prec' : prec
    }
    lista_produtos.append(prod_dict)
    print()



#Consulta produto
def consultar_produtos():
    while True:
        try:
            if not lista_produtos:
                print('Nâo existem produtos cadastrados!\n')
                break
            else:

                    print("Bem-vindo a CONSULTA de Produtos:\n"
                          "\t1) Consultar Todos os produtos\n"
                          "\t2) Consultar Produto por Código\n"
                          "\t3) Consultar Produto(s) por Fabricante\n"
                          "\t4) Retornar")

                    x = int(input('>>> '))

                    if x == 1:
                        print('Ok, vamos lá!')
                        for i in range(3):
                            print('. ', end='')
                            sleep(0.5)

                        print()
                        print()

                        for k, v in enumerate(lista_produtos):
                            print(f'Cod --> {v.get("cod")}: Prod = {v.get("prod")}, Fab = {v.get("fab")}, Preço = {v.get("prec")}\n')
                    elif x == 2:
                        c = int(input('Informe o código do produto: '))
                        for k, v in enumerate(lista_produtos):
                            if k + 1 == c:
                                print(f'Cod --> {v.get("cod")}: Prod = {v.get("prod")}, Fab = {v.get("fab")}, Preço = {v.get("prec")}\n')
                    elif x == 3:
                        local = 0
                        produto = input('Informe o nome do Fabricante: ')
                        for k, v in enumerate(lista_produtos):
                            if v.get('fab') == produto:
                                local = k
                        print('Realizando a busca!')
                        for i in range(3):
                            print('. ', end='')
                            sleep(0.5)
                        print()
                        print()

                        for k, v in enumerate(lista_produtos):
                            if k == local:
                                print(f'Cod --> {v.get("cod")}: Prod = {v.get("prod")}, Fab = {v.get("fab")}, Preço = R${v.get("prec")}\n')

                    elif x == 4:
                        return False

                    else:
                        ...
        except ValueError:
            print('VALOR INVÁLIDO - Apenas "1", "2", "3" e "4"!\n')
            break


# Cadastrar produto
def remover_produtos():
    while True:
        try:
            opt = int(input("Bem-vindo a EXCLUSÂO de Produtos\n"
                        "\t1) Para informar o código do produto que será removido\n"
                        "\t2) Para voltar ao menu principal\n"
                        "\t>>> "))

            if opt == 1:
                esc = int(input('Informe o código do produto que será excluído: '))
                dec = input('Tem certeza que deseja continuar? (S/N) ').upper()
                if dec == 'S':
                    lista_produtos[:] = [d for d in lista_produtos if d.get('cod') != esc]
            else:
               break

        except ValueError:
            print('Valor inválido!')

#Inicio MAIN
cod_prod = 0
print("Bem-vindo ao Programa Controle de Produtos")
while True:
    try:
        op = int(input("Digite a opção desejada:\n"
                       "1) Cadastrar Produto\n"
                       "2) Consultar Produto(s)\n"
                       "3) Remover Produto\n"
                       "4) Sair\n"
                       ">>> "))
        print()

        if op == 1:
            cod_prod += 1
            cadastrar_produtos(cod_prod)
        elif op == 2:
            consultar_produtos()
        elif op == 3:
            remover_produtos()
        elif op == 4:
            print('Programa finalizado!')
            break
        else:
            continue

    except:
        print('São permitidos apenas números inteiros!')
        print()


#Fim MAIN
