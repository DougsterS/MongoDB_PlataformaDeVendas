import time
from classesMongo.Venda import Venda
from pymongo import MongoClient

bd = MongoClient("mongodb://localhost:27017") #estabelece conexão com o banco
banco = bd['VendasAPP'] #faz uso ddo banco

def menuVendas():
    opcaoVendas = 0
    while(opcaoVendas >= 0) and (opcaoVendas<=4):
        print('\n====AREA DE VENDAS====\n')
        print('O que deseja fazer?\n\t1 - Realizar Venda\n\t2 - Historico de Vendas'
              '\n\t3 - Consultar Nota Fiscal de Venda\n\t4 - Apagar Venda'
              '\n\t0 - Retornar ao Menu Principal')
        try:
            opcaoVendas = int(input('Digite tua opcao:'))
        except:
            print('Acao Incoerente')
            opcaoVendas=0

        if(opcaoVendas==1):
            print('\n====CENTRAL DE TRANSACAO====\n')
            print('Informe o CPF do Cliente que deseja realizar a compra')
            cpfCliente = input('CPF: ')

            cliente = banco.clientes
            doc = cliente.find_one({'CPF': cpfCliente})
            if (doc is None):
                print(f'O CPF {cpfCliente} nao consta no sistema')
            else:
                print('Informe o codigo de produto que o cliente deseja comprar')
                codProd = input('Codigo de Produto: ')

                produtos = banco.produtos
                doc2 = produtos.find_one({'Codigo':codProd})

                if(doc2 is None):
                    print(f'O produto {codProd} nao esta cadastrado no sistema')

                else:
                    print('Informe o numero da venda:')
                    realizaVenda = Venda()
                    realizaVenda.NumVenda = input('Digite o numero da venda: ')

                    realizaVenda.realizaVenda(codProduto=codProd,idCliente=cpfCliente)
            time.sleep(2)


        elif(opcaoVendas==2):
            historicoVendas = Venda()
            print('\n====HISTORICO DE VENDAS====\n')
            historicoVendas.historicoVenda()
            print('=============================')
            time.sleep(2)


        elif(opcaoVendas==3):
            consultaVenda = Venda()
            print('\n====CONSULTOR DE NOTA FISCAL====\n')
            print('Por favor, insira o numero da venda que deseja emitir nota')
            notaFiscal = input('Numero Venda: ')
            consultaVenda.consultaVenda(notaFiscal)
            time.sleep(2)
            opcaoVendas - -1

        elif(opcaoVendas==4):
            removeVenda = Venda()
            print('\n====REMOCAO DE VENDA====\n')
            print('Informe o numero da venda que deseja apagar: ')
            numVenda = input('Numero da Venda: ')
            removeVenda.apagarVenda(numVenda)
            time.sleep(2)


        elif(opcaoVendas==0):
            print('Retornando ao Menu Principal')
            time.sleep(2)
            opcaoVendas = -1

        else:
            print('Por favor insira um valor valido')
            opcaoVendas = 0