'''
Classe responsável por conter a classe Fornecedor e todas as acoes ligadas aos mesmos
'''

from pymongo import MongoClient

bdFornecedor = MongoClient("mongodb://localhost:27017") #estabelece conexão com o banco
banco = bdFornecedor['VendasAPP'] #faz uso ddo banco

class Fornecedor(object):
    def listaFornecedor(self): #Exibe todos os fornecederoes do sistema:
        fornecedores = banco.fornecedores
        for doc in fornecedores.find():
            print(f'Fornecedor: {doc["Nome"]}\nCNPJ: {doc["CNPJ"]}\nTipo de Produto: {doc["TipoProdutos"]}\nEmail: {doc["Email"]}\n')

    def procuraFornecedor(self, idFornecedor):#procura um fornecedor especifico
        fornecedores = banco.fornecedores
        doc = fornecedores.find_one({'CNPJ': idFornecedor})
        if (doc is None):
            print(f'O CNPJ {idFornecedor} nao consta no sistema')
        else:
            print(f'Fornecedor: {doc["Nome"]}\nCNPJ: {doc["CNPJ"]}\nTipo de Produto: {doc["TipoProdutos"]}\nEmail: {doc["Email"]}\n')


    def insereFornecedor(self):#cria um novo fornecedor
        fornecedor = {
            "Nome": self.Nome,
            "CNPJ": self.CNPJ,
            "TipoProdutos": self.TipoProdutos,
            "Email": self.Email
        }

        fornecedores = banco.fornecedores  # acessar a colecao fornecedores dentro do banco
        fornecedores.insert_one(fornecedor)  # faz a isercao dos dados do fornecedor no banco
        print(f'Fornecedor {fornecedor["Nome"]} inserido com sucesso!')

    def removeFornecedor(self, idFornecedor): #realiza a remocao de um dito fornecedor
        fornecedores = banco.fornecedores
        doc = fornecedores.find_one({'CNPJ':idFornecedor})
        if(doc is None):
            print(f'O CNPJ {idFornecedor} nao consta no sistema')
        else:
            print(f'Tem certeza que deseja excluir {doc["Nome"]}?\n\t1 - SIM\n\t2 - NAO')
            try:
                opcaoRemocao = int(input('Digite tua opcao: '))
            except ValueError:
                opcaoRemocao = -1
            if(opcaoRemocao==1):
                fornecedores.delete_one({'CNPJ':idFornecedor})
                print(f'O fornecedor {doc["Nome"]} de CNPJ {doc["CNPJ"]} foi removido com sucesso do sistema!')
            else:
                print('Operacao Cancelada')


    def atualizaFornecedor(self, idFornecedor, dado, valor): #Atualiza informacao de um dito fornecedor
        fornecedores = banco.fornecedores
        doc = fornecedores.find_one({'CNPJ': idFornecedor})
        if (doc is None):
            print(f'O CNPJ {idFornecedor} nao consta no sistema')
        else:
            fornecedores.update_one({'CNPJ':idFornecedor},{
                "$set" : {f'{dado}': valor}
            })
            print(f'{doc["Nome"]} alterado no CNPJ {doc["CNPJ"]}')

    def fornecedorJson(self,idFornecedor):
        fornecedores = banco.fornecedores
        doc = fornecedores.find_one({'CNPJ': idFornecedor})
        if (doc is None):
            print(f'O CNPJ {idFornecedor} nao consta no sistema')
        else:
            return doc