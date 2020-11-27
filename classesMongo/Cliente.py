'''
Classe responsável por conter a classe Cliente e todas as acoes ligadas aos mesmos
'''

from pymongo import MongoClient

bdCliente = MongoClient("mongodb://localhost:27017") #estabelece conexão com o banco
banco = bdCliente['VendasAPP'] #faz uso do banco

class Cliente(object):
    def todosClientes(self):#Exibir todos os clientes do sistema
        clientes = banco.clientes#variavel para acessar colecao clientes no banco
        for doc in clientes.find():
            print(f"Nome: {doc['Nome']}\nCPF: {doc['CPF']}\nData de Nascimento: {doc['DtNascimento']}\nEmail: {doc['Email']}\n")

    def procuraCliente(self, cpfCliente):#Fazer a busca de cliente especifico
        clientes = banco.clientes#variavel para acessar colecao clientes no banco
        doc = clientes.find_one({"CPF": cpfCliente})
        if(doc is None):
            print(f'O cpf {cpfCliente} nao consta no sistema')
        else:
            print(f"Nome: {doc['Nome']}\nCPF: {doc['CPF']}\nData de Nascimento: {doc['DtNascimento']}\nEmail: {doc['Email']}\n")

    def insereCliente(self):#cria um novo cliente
        cliente ={
            "Nome": self.Nome,
            "CPF": self.CPF,
            "DtNascimento": self.DtNascimento,
            "Email": self.Email
        }

        clientes = banco.clientes#variavel pra acessar uma coleção clientes no banco
        clientes.insert_one(cliente)#inserção do dados
        print(f"Cliente {cliente['Nome']} inserido com sucesso")

    def removeCliente(self,cpfCliente):#remove cliente
        clientes = banco.clientes
        doc = clientes.find_one({'CPF': cpfCliente})
        if (doc is None):
            print(f'O CPF {cpfCliente} nao consta no sistema')
        else:
            print(f'Tem certeza que deseja excluir {doc["Nome"]}?\n\t1 - Sim\n\t2 - Nao')
            try:
                opcaoRemocao = int(input('Digite tua opcao: '))
            except ValueError:
                opcaoRemocao = -1
            if(opcaoRemocao==1):
                clientes.delete_one({'CPF': cpfCliente})
                print(f'O usuario {doc["Nome"]} de CPF {cpfCliente} foi removido com sucesso do sistema!')
            else:
                print('Operacao cancelada')


    def atualizaCliente(self,cpfCliente,dado,valor):#atualiza clientes
        clientes = banco.clientes
        doc = clientes.find_one({'CPF': cpfCliente})
        if(doc is None):
            print(f'O CPF {cpfCliente} nao consta no sistema')

        else:
            clientes.update_one({'CPF': cpfCliente},{
                "$set" : {
                    f'{dado}': valor
            }
            })
            print(f'{doc["Nome"]} alterado com sucesso no CPF {doc["CPF"]}')

    def clienteJson(self,cpf):
        clientes = banco.clientes
        doc = clientes.find_one({'CPF': cpf})
        if (doc is None):
            print(f'O CNPJ {cpf} nao consta no sistema')
        else:
            return doc
