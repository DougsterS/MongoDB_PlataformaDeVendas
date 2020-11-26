import time
from classesMongo.Fornecedor import Fornecedor

def menuFornecedores():
    opcaoFornecedores = 0
    while(opcaoFornecedores >= 0) and (opcaoFornecedores<=5):
        print('\n====AREA DE FORNECEDORES====\n')
        print('O que deseja fazer?\n\t1 - Cadastrar novo fornecedor\n\t2 - Listar os Fornecedores disponiveis'
              '\n\t3 - Buscar Fornecedor especifico\n\t4 - Atualizar Fornecedor existente\n\t5 - Remover Fornecedor'
              '\n\t0 - Retornar ao Menu Principal')
        try:
            opcaoFornecedores = int(input('Digite tua opcao:'))
        except:
            print('Acao Incoerente')
            opcaoFornecedores=0

        if(opcaoFornecedores==1):
            novoFornecedor = Fornecedor()
            print('\n====CRIACAO FORNECEDOR====\n')
            novoFornecedor.Nome = input('Digite o nome do fornecedor: ')
            novoFornecedor.CNPJ = input('Digite o CNPJ do fornecedor: ')
            novoFornecedor.TipoProdutos = input('Informe o tipo de produto do fornecedor: ')
            novoFornecedor.Email = input('Informe email para contato: ')

            novoFornecedor.insereFornecedor()
            print('\nRetornando ao Menu Principal')
            time.sleep(2)
            opcaoFornecedores = -1

        elif(opcaoFornecedores==2):
            lerFornecedores = Fornecedor()
            print('\n====LISTA DE FORNECEDORES====\n')
            lerFornecedores.listaFornecedor()
            print('\nRetornando ao Menu Principal')
            time.sleep(2)
            opcaoFornecedores = -1

        elif(opcaoFornecedores==3):
            consultaFornecedor = Fornecedor()
            print('\n====CONSULTA DE FORNECEDOR====\n')
            consulta = input('Digite o CNPJ do Fornecedor que deseja consultar: ')
            consultaFornecedor.procuraFornecedor(consulta)
            time.sleep(2)
            opcaoFornecedores = -1

        elif(opcaoFornecedores==4):
            atualizaFornecedor = Fornecedor()
            print('\n====ATUALIZAR FORNECEDOR====\n')
            print('Por favor informe o CNPJ que deseja alterar')
            cnpj = input('CNPJ: ')
            print(f'Qual alteracao deseja fazer no CNPJ {cnpj}?\n\t1 - Alterar Nome\n\t2 - Alterar CNPJ'
                  f'\n\t3 - Alterar tipo de produto\n\t4 - Alterar Email')
            try:
                opcaoAtualiza = int(input('Digite tua opcao: '))
            except ValueError:
                opcaoAtualiza = -1
                opcaoFornecedores = -1

            if (opcaoAtualiza == 1):
                novoNome = input('Digite o novo nome: ')
                atualizaFornecedor.atualizaFornecedor(cnpj, dado='Nome', valor=novoNome)

            elif (opcaoAtualiza == 2):
                novoCNPJ = input('Digite o novo CNPJ: ')
                atualizaFornecedor.atualizaFornecedor(cnpj, dado='CNPJ', valor=novoCNPJ)

            elif(opcaoAtualiza==3):
                novoProduto = input('Digite o novo tipo de produto fornecido: ')
                atualizaFornecedor.atualizaFornecedor(cnpj, dado='TipoProdutos',valor=novoProduto)

            elif(opcaoAtualiza == 4):
                novoEmail = input('Digite o novo email do fornecedor: ')
                atualizaFornecedor.atualizaFornecedor(cnpj, dado='Email',valor=novoEmail)

            else:
                print('Opcao invalida, retornando ao menu principal')
            time.sleep(2)

        elif(opcaoFornecedores==5):
            removeFornecedor = Fornecedor()
            print('\n====REMOCAO DE FORNECEDOR====\n')
            print('Digite o CNPJ que deseja remover do sistema')
            cnpj = input('CNPJ: ')
            removeFornecedor.removeFornecedor(cnpj)
            time.sleep(2)

        elif(opcaoFornecedores==0):
            print('Retornando ao Menu Principal')
            time.sleep(2)
            opcaoFornecedores = -1

        else:
            print('Por favor insira um valor valido')
            opcaoFornecedores = 0