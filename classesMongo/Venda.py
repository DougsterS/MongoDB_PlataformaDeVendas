'''
Classe responsável por conter a classe Venda e todas as acoes ligadas aos mesmos
'''

import time
from pymongo import MongoClient
from classesMongo.Produto import Produto
from classesMongo.Cliente import Cliente

bdVendas = MongoClient("mongodb://localhost:27017") #estabelece conexão com o banco
banco = bdVendas['VendasAPP'] #faz uso ddo banco

class Venda(object):

    def realizaVenda(self, codProduto, idCliente):
        encontraCliente = Cliente()
        encontraProduto = Produto()

        clientes = banco.clientes
        produtos = banco.produtos

        venda = {
            'NumVenda': self.NumVenda,
            'Produto': encontraProduto.produtoJson(codProduto),
            'Cliente': encontraCliente.clienteJson(idCliente)
        }

        docProd = produtos.find_one({'Codigo': codProduto})
        docCliente = clientes.find_one({'CPF': idCliente})
        print(f'\nNumero de Venda: {venda["NumVenda"]}\nProduto Vendido: {docProd["Nome"]}\nComprador: {docCliente["Nome"]}'
              f'\nCPF do Comprador: {docCliente["CPF"]}\nPreco da Compra: {docProd["Preco"]}\n')
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
            doc2 = doc["Produto"]
            doc3 = doc["Cliente"]
            print(f'Numero de Venda: {doc["NumVenda"]}\nProduto Vendido: {doc2["Nome"]}\nComprador: {doc3["Nome"]}'
                  f'\nCPF do Comprador: {doc3["CPF"]}\nPreco da Compra: {doc2["Preco"]}\n')

    def consultaVenda(self, numVenda):
        vendas = banco.vendas
        doc = vendas.find_one({'NumVenda' : numVenda})
        if (doc is None):
            print(f'A venda {numVenda} nao existe!!!')

        else:
            doc2 = doc["Produto"]
            doc3 = doc["Cliente"]
            print(f'\nNOTA FISCAL\n\tNumero de Venda: {doc["NumVenda"]}\n\tProduto Vendido: {doc2["Nome"]}\n\tComprador: {doc3["Nome"]}'
                f'\n\tCPF do Comprador: {doc3["CPF"]}\n\tPreco da Compra: {doc2["Preco"]}\n')

    def apagarVenda(self, numVenda):
        vendas = banco.vendas
        doc = vendas.find_one({'NumVenda':numVenda})
        if (doc is None):
            print(f'A venda {numVenda} nao existe no sistema!')

        else:
            doc2=doc["Cliente"]
            print(f'Tem certeza que deseja excluir a venda {doc["NumVenda"]} do comprador \n'
                  f'{doc2["Nome"]} sob o CPF {doc2["CPF"]}?\n\t1 - SIM\n\t2 - NAO'
                  f'\nOBS: ESTA ACAO NAO PODE SER DESFEITA')
            try:
                opcaoRemocap = int(input('Opcao: '))

            except ValueError:
                opcaoRemocap = -1

            if(opcaoRemocap==1):
                vendas.delete_one({"NumVenda":numVenda})
                print(f'A venda {doc["NumVenda"]} do Cliente {doc2["Nome"]} foi removida dom sucesso!!!')

            else:
                print('OPERACAO CANCELADA!!!')