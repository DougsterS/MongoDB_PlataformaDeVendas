import time
from classesMongo.Produto import Produto
from pymongo import MongoClient

bd = MongoClient("mongodb://localhost:27017") #estabelece conexão com o banco
banco = bd['VendasAPP'] #faz uso ddo banco

def menuProdutos():
    opcaoProdutos = 0
    while(opcaoProdutos >= 0) and (opcaoProdutos<=5):
        print('\n====AREA DE PRODUTOS====\n')
        print('O que deseja fazer?\n\t1 - Cadastrar novo produto\n\t2 - Listar os Produtos em estoque'
              '\n\t3 - Buscar produto\n\t4 - Atualizar produto\n\t5 - Remover produto'
              '\n\t0 - Retornar ao Menu Principal')
        try:
            opcaoProdutos = int(input('Digite tua opcao:'))
        except:
            print('Acao Incoerente')
            opcaoFornecedores=0

        if(opcaoProdutos==1):
            print('\n====CADASTRO DE PRODUTO====\n')
            print('Informe o CNPJ o qual deseja atribuir o produto:')
            cnpj = input('CNPJ: ')

            fornecedor = banco.fornecedores#acessar o banco de fornecedores para saber se o cnpj esta cadastrado
            doc = fornecedor.find_one({'CNPJ': cnpj})

            if(doc is None):
                print(f'O CNPJ {cnpj} nao consta no sistema, retornando para area de produtos')
                time.sleep(2)

            else:
                novoProduto = Produto()
                novoProduto.Nome = input('Digite o Nome do Produto: ')
                novoProduto.Codigo = input('Atribua um codigo ao produto: ')
                novoProduto.Preco = input('Preco do Produto: ')

                novoProduto.criaProduto(cnpj)
                time.sleep(2)

        elif(opcaoProdutos==2):
            lerProdutos = Produto()
            print('\n====PRODUTOS DO SISTEMA====\n')
            lerProdutos.listaProduto()
            print('Retornando ao Menu Principal')
            time.sleep(2)
            opcaoProdutos = -1

        elif(opcaoProdutos==3):
            consultaProduto = Produto()
            print('\n====CONSULTA DE PRODUTO====\n')
            print('Digite o codigo de produto que deseja checar')
            consulta = input('Codigo: ')
            consultaProduto.procuraProduto(consulta)
            time.sleep(2)

        elif(opcaoProdutos==4):
            atualizaProduto = Produto()
            print('\n====ATUALIZAR PRODUTO====\n')
            print('Por favor informe o Codigo do produto que deseja alterar')
            codigoProduto = input('Codigo: ')

            produtos = banco.produtos
            doc = produtos.find_one({'Codigo': codigoProduto})

            if(doc is None):
                print(f'O codigo {codigoProduto} nao consta no sistema')

            else:
                print(f'Informe qual operacao deseja realizar em {doc["Nome"]}\n\t1 - Alterar Nome\n\t2 - Alterar Codigo'
                      f'\n\t3 - Alterar preco\n\t4 - Alterar fornecedor')
                try:
                    opcaoAtualiza = int(input('Opcao: '))
                except ValueError:
                    opcaoAtualiza = -1

                if(opcaoAtualiza == 1):
                    novoNome = input('Digite o novo nome: ')
                    atualizaProduto.atualizaProduto(codigoProduto,dado='Nome',valor=novoNome)

                elif(opcaoAtualiza == 2):
                    novoCod = input('Digite o novo codigo: ')
                    atualizaProduto.atualizaProduto(codigoProduto,dado='Codigo',valor=novoCod)

                elif(opcaoAtualiza == 3):
                    print(f'O preco atual e: {doc["Preco"]}')
                    novoPreco = input('Digite o novo preco: ')
                    atualizaProduto.atualizaProduto(codigoProduto,dado='Preco',valor=novoPreco)

                elif(opcaoAtualiza == 4):
                    novoFornecedor = input('Digite o CNPJ do novo fornecedor: ')

                    fornecedor = banco.fornecedores#acessar banco do fornecedor
                    doc2 = fornecedor.find_one({'CNPJ': novoFornecedor})#encontrar dados do fornecedor

                    if(doc2 is None):
                        print(f'O CNPJ {novoFornecedor} nao esta inserido no sistema')

                    else:
                        atualizaProduto.atualizaProduto(codigoProduto, dado='Fornecedor',valor=doc2)

                else:
                    print('Opcao Invalida')
                time.sleep(2)

        elif(opcaoProdutos==5):
            removeProduto = Produto()
            print('\n====REMOCAO DE PRODUTO====\n')
            print('Digite o codigo de produto que deseja remover do sistema')
            codProduto = input('Codigo: ')
            removeProduto.removeProduto(codProduto)
            time.sleep(2)

        elif(opcaoProdutos==0):
            print('Retornando ao Menu Principal')
            time.sleep(2)
            opcaoProdutos = -1

        else:
            print('Por favor insira um valor valido')
            opcaoProdutos = 0