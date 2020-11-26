'''
Classe responsável por conter a classe Venda e todas as acoes ligadas aos mesmos
'''

import time
from pymongo import MongoClient

bdVendas = MongoClient("mongodb://localhost:27017") #estabelece conexão com o banco
banco = bdVendas['VendasAPP'] #faz uso ddo banco

class Venda(object):

    def realizaVenda(self, codProduto, idCliente):
        clientes = banco.clientes
        produtos = banco.produtos
        doccliente = clientes.find_one({'CPF':idCliente})
        docprod = produtos.find_one({'Codigo': codProduto})

        venda = {
            'NumVenda': self.NumVenda,
            'Produto': docprod['Nome'],
            'PrecoTotal' : docprod['Preco'],
            'NomeCliente' : doccliente['Nome'],
            'CPFCliente' : doccliente['CPF']
        }

        print(f'\nNumero de Venda: {venda["NumVenda"]}\nProduto Vendido: {venda["Produto"]}\nComprador: {venda["NomeCliente"]}'
              f'\nCPF do Comprador: {venda["CPFCliente"]}\nPreco da Compra: {venda["PrecoTotal"]}\n')
        time.sleep(2)
        print('Deseja Finalizar a venda?\n\t1 - SIM\n\t2 - NAO')
        try:
            fimVenda = int(input('Opcao: '))
        except ValueError:
            fimVenda = -1

        if(fimVenda == 1):
            vendas = banco.vendas
            vendas.insert_one(venda)
            print(f'A venda {venda["NumVenda"]} foi realizada com sucesso!')

        else:
            print('VENDA CANCELADA!!!!')

    def historicoVenda(self):
        vendas = banco.vendas
        for doc in vendas.find():
            print(f'Numero de Venda: {doc["NumVenda"]}\nProduto Vendido: {doc["Produto"]}\nComprador: {doc["NomeCliente"]}'
                  f'\nCPF do Comprador: {doc["CPFCliente"]}\nPreco da Compra: {doc["PrecoTotal"]}\n')

    def consultaVenda(self, numVenda):
        vendas = banco.vendas
        doc = vendas.find_one({'NumVenda' : numVenda})
        if (doc is None):
            print(f'A venda {numVenda} nao existe!!!')

        else:
            print(f'\nNOTA FISCAL\n\tNumero de Venda: {doc["NumVenda"]}\n\tProduto Vendido: {doc["Produto"]}\n\tComprador: {doc["NomeCliente"]}'
                f'\n\tCPF do Comprador: {doc["CPFCliente"]}\n\tPreco da Compra: {doc["PrecoTotal"]}\n')

    def apagarVenda(self, numVenda):
        vendas = banco.vendas
        doc = vendas.find_one({'NumVenda':numVenda})
        if (doc is None):
            print(f'A venda {numVenda} nao existe no sistema!')

        else:
            print(f'Tem certeza que deseja excluir a venda {doc["NumVenda"]} do comprador \n'
                  f'{doc["NomeCliente"]} sob o CPF {doc["CPFCliente"]}?\n\t1 - SIM\n\t2 - NAO'
                  f'\nOBS: ESTA ACAO NAO PODE SER DESFEITA')
            try:
                opcaoRemocap = int(input('Opcao: '))

            except ValueError:
                opcaoRemocap = -1

            if(opcaoRemocap==1):
                vendas.delete_one({"NumVenda":numVenda})
                print(f'A venda {doc["NumVenda"]} do Cliente {doc["NomeCliente"]} foi removida dom sucesso!!!')

            else:
                print('OPERACAO CANCELADA!!!')