"""
1 - Clientes
2 - Fonecedores
3 - Produtos
4 - Vendas
"""
import time
from menusInteracoes.MenuClientes import menuClientes
from menusInteracoes.MenuFornecedores import menuFornecedores
from menusInteracoes.MenuProdutos import menuProdutos
from menusInteracoes.MenuVendas import menuVendas

opcao = 0
while(opcao>=0) and (opcao<=4):#Menu Principal
    print('\n====MENU PRINCIPAL====\n')
    print('Selecione a opcao que deseja utilizar')
    print('\t1 - Cliente')
    print('\t2 - Fornecedores')
    print('\t3 - Produtos')
    print('\t4 - Vendas')
    print('\t5 - Sair do programa')
    try:
        opcao = int(input('Digite tua opcao: '))
    except ValueError:
        opcao = 0

    if(opcao==0):
        print('Digite um valor valido....')

    elif(opcao==1):
        menuClientes()

    elif (opcao == 2):
        menuFornecedores()

    elif (opcao == 3):
        menuProdutos()

    elif (opcao == 4):
        menuVendas()

    else:
        print('Encerrando o Sistema...')
        time.sleep(2)
