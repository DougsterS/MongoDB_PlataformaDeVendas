import time
from classesMongo.Cliente import Cliente

def menuClientes():
    opcaoCliente = 0
    while (opcaoCliente >= 0) and (opcaoCliente <= 5):  # Menu do Cliente
        print('\n====AREA DO CLIENTE====\nO que deseja fazer?\n\t1 - Criar Cliente'
              '\n\t2 - Listar todos os Clientes\n\t3 - Buscar Cliente\n\t4 - Atualizar dados de Cliente'
              '\n\t5 - Remover Cliente\n\t0 - Retornar ao menu principal')

        try:
            opcaoCliente = int(input('Digite tua opcao: '))
        except ValueError:
            print('Acao Incoerente')
            opcaoCliente = 0

        if (opcaoCliente == 0):  # Menu principal
            print('Redirecionando ao Menu Principal')
            opcaoCliente = -1
            opcao = 0
            time.sleep(2)

        elif (opcaoCliente == 1):  # insercao de dados do cliente
            novoCliente = Cliente()
            print('\n====CRIACAO DE CLIENTE====\n')
            novoCliente.Nome = input('Digite o nome do novo cliente: ')
            novoCliente.CPF = input('Digite o CPF do novo cliente: ')
            novoCliente.DtNascimento = input('Digite a data de nascimento do novo cliente: ')
            novoCliente.Email = input('Digite o email do cliente: ')

            novoCliente.insereCliente()
            print('\nRetornando ao Menu Principal')
            time.sleep(2)
            opcaoCliente = -1

        elif (opcaoCliente == 2):  # lista de clientes
            lerClientes = Cliente()
            print('\n====LISTA DE CLIENTES CADASTRADOS====\n')
            lerClientes.todosClientes()
            print('\nRetornando ao Menu Principal')
            time.sleep(2)
            opcaoCliente = -1

        elif (opcaoCliente == 3):  # Busca de cliente
            consultaClientes = Cliente()
            print('\n====CONSULTA DE CLIENTE====\n')
            cpf = input('Digite o CPF que deseja buscar: ')
            consultaClientes.procuraCliente(cpf)
            time.sleep(2)
            opcaoCliente = -1

        elif (opcaoCliente == 4):  # Atualizacao de Cliente
            alteraCliente = Cliente()
            print('\n====ATUALIZACAO DE CLIENTE====\n')
            print('Por favor, informe o CPF que deseja alterar')
            cpf = input('CPF: ')
            print(
                f'Qual alteracao deseja fazer no CPF {cpf}?\n\t1 - Alterar Nome\n\t2 - Alterar CPF\n\t3 - Alterar Data de Nascimento'
                f'\n\t4 - Alterar email')
            try:
                opcaoDeAtualizar = int(input('Digite tua opcao: '))
            except ValueError:
                opcaoDeAtualizar = -1
                opcaoCliente = -1

            if (opcaoDeAtualizar == 1):
                novoNome = input('Digite o novo nome: ')
                alteraCliente.atualizaCliente(cpf, dado='Nome', valor=novoNome)

            elif (opcaoDeAtualizar == 2):
                novoCPF = input('Digite o novo CPF: ')
                alteraCliente.atualizaCliente(cpf, dado='CPF', valor=novoCPF)

            elif (opcaoDeAtualizar == 3):
                novaData = input('Digite a nova Data de Nascimento: ')
                alteraCliente.atualizaCliente(cpf, dado='DtNascimento', valor=novaData)

            elif (opcaoDeAtualizar == 4):
                novoEmail = input('Digite o novo email: ')
                alteraCliente.atualizaCliente(cpf, dado='Email', valor=novoEmail)

            else:
                print('Opcao Invalida, retornando ao Menu Principal')
                opcaoCliente = -1
            time.sleep(2)

        elif (opcaoCliente == 5):  # Remocao do cliente
            removeCliente = Cliente()
            print('\n====REMOCAO DE CLIENTE====\n')
            print('Digite o CPF que deseja remover do sistema:')
            cpf = input('CPF: ')
            removeCliente.removeCliente(cpf)
            time.sleep(2)

        else:
            print('Por favor, insira um valor valido')
            opcaoCliente = 0