"""
IMPORTANTE = Python v 3.10
EXERCICIO 4
"""
#Lista
lista_produtos = []

# Funções
# Cadastrar estudante
def cadastrar_produtos():
    print("Bem-vindo ao CADASTRO de Produtos")


#Consulta estudantes
def consultar_produtos():
    print("Bem-vindo a CONSULTA de Produtos")


# Cadastrar estudante
def remover_produtos():
    print("Bem-vindo a EXCLUSÂO de Produtos")


#Teste int
def testa_num(n):
    try:
        int(n)
        return int(n)
    except ValueError:
        return False


#Começo MAIN
lista_opcoes = [1, 2, 3, 4]
print("Bem-vindo ao Programa Controle de Produtos")
while True:
    op = input("Digite a opção desejada:\n"
                   "1) Consultar Todas as Produto\n"
                   "2) Consultar Produto por Código\n"
                   "3) Consultar Produto(s) por Fabricante\n"
                   "4) Retornar\n"
                   ">>> ")
    print()

    op = testa_num(op)
    if op in lista_opcoes:
        pass
    else:
        print('Apenas os números "1", "2", "3" e "4"')

    if op == 1:
        cadastrar_produtos()
    elif op == 2:
        consultar_produtos()
    elif op == 3:
        remover_produtos()
    elif op == 4:
        print('Programa finalizado!')
        break




#Fim MAIN
