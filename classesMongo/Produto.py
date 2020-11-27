'''
Classe responsável por conter a classe Produto e todas as acoes ligadas aos mesmos
'''

from pymongo import MongoClient
from classesMongo.Fornecedor import Fornecedor

bdProduto = MongoClient("mongodb://localhost:27017") #estabelece conexão com o banco
banco = bdProduto['VendasAPP'] #faz uso ddo banco

class Produto(object):

    def criaProduto(self,cnpjFornecedor):

        lerFornecedor=Fornecedor()

        produto = {
            'Nome': self.Nome,
            'Codigo': self.Codigo,
            'Preco': self.Preco,
            'Fornecedor': lerFornecedor.fornecedorJson(idFornecedor=cnpjFornecedor)
        }

        produtos = banco.produtos
        produtos.insert_one(produto)#faz a insercao do produto
        print(f'O produto {produto["Nome"]} foi cadastrado no sistema')

    def listaProduto(self):
        produtos = banco.produtos
        for doc in produtos.find():
            doc2 = doc["Fornecedor"]
            print(f'Produto: {doc["Nome"]}\nCodigo do Produto: {doc["Codigo"]}\nPreco: {doc["Preco"]}\n'
                  f'Fornecedor: {doc2["Nome"]}\nCNPJ Do Fornecedor: {doc2["CNPJ"]}')

    def procuraProduto(self,codProduto):
        produtos = banco.produtos
        doc = produtos.find_one({'Codigo': codProduto})
        if (doc is None):
            print(f'Nao existe produto de codigo {codProduto} no sistema')
        else:
            doc2 = doc["Fornecedor"]
            print(f'\nProduto: {doc["Nome"]}\nCodigo do Produto: {doc["Codigo"]}\nPreco: {doc["Preco"]}'
                  f'\nFornecido por: {doc2["Nome"]}\nCNPJ do Fornecedor: {doc2["CNPJ"]}\n')

    def atualizaProduto(self, codProduto, dado, valor):
        produtos = banco.produtos
        doc = produtos.find_one({'Codigo':codProduto})
        if (doc is None):
            print(f'O codigo {codProduto} nao consta no sistema')
        else:
            produtos.update_one({'Codigo':codProduto},{
                '$set' : {f'{dado}': valor}
            })

            print(f'O Produto {doc["Nome"]} foi alterado no codigo {doc["Codigo"]}')

    def removeProduto(self, codProduto):
        produtos = banco.produtos
        doc = produtos.find_one({'Codigo':codProduto})
        if (doc is None):
            print(f'O codigo {codProduto} nao esta atribuido a nenhum produto')
        else:
            print(f'Tem certeza que deseja excluir {doc["Nome"]}?\n\t1 - SIM\n\t2 - NAO')
            try:
                opcaoRemocao = int(input('Opcao: '))
            except ValueError:
                opcaoRemocao = -1

            if(opcaoRemocao == 1):
                produtos.delete_one({'Codigo':codProduto})
                print(f'O produto {doc["Nome"]} foi removido com sucesso do sistema!')

            else:
                print('Operacao cancelada!!!')

    def produtoJson(self,idProduto):
        produtos = banco.produtos
        doc = produtos.find_one({'Codigo': idProduto})
        if (doc is None):
            print(f'O CNPJ {idProduto} nao consta no sistema')
        else:
            return doc