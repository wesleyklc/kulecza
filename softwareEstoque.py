lista_peca = []  # Criação de uma lista vazia
codigo_peca = 0  # Variável para ser usada nos códigos das peças


def cadastrarPeca(codigo):  # Função para cadastrar as peças
    nome = input('Digite o nome da peça: ')
    fabricante = input('Digite o fabricante da peça: ')
    valor = float(input('Digite o valor da peça: '))
    dicionario_peca = {'codigo': codigo, 'nome': nome, 'fabricante': fabricante, 'valor': valor}  # Criação de um dicionário para armazenar os dados
    lista_peca.append(dicionario_peca.copy())  # Cópia do dicionário dentro da lista


def consultarPeca():  # Função para consultar as peças cadastradas
    while True:
        consulta = input('\nDigite a opção desejada: \n'
                         '1 - Consultar todas as peças \n'
                         '2 - Consultar peças por código \n'
                         '3 - Consultar peças por fabricante \n'
                         '4 - Retornar \n'
                         '>> ')
        if consulta == '1':
            print('Você escolheu a opção CONSULTAR TODOS AS PEÇAS')
            for peca in lista_peca:  # Varrer toda a lista
                print('-' * 20)
                for key, values in peca.items():  # Varrer cada item
                    print('{}: {}'.format(key, values))
        elif consulta == '2':
            print('Você escolheu a opção CONSULTAR PEÇAS POR CÓDIGO ')
            codigo_desejado = int(input('Digite o código desejado: '))
            for codigo in lista_peca:  # Varrer toda a lista
                if codigo['codigo'] == codigo_desejado:  # Verificar se o código desejado está no dici-onário
                    print('-' * 20)
                    for key, values in codigo.items():  # Varrer cada item
                        print('{}: {}'.format(key, values))
        elif consulta == '3':
            print('Você escolheu a opção CONSULTAR PEÇAS POR FABRICANTE')
            fabricante_desejado = input('Digite o fabricante desejado: ')
            for fabricante in lista_peca:  # Varrer toda a lista
                if fabricante['fabricante'] == fabricante_desejado:  # Verificar se o fabricante deseja-do está no dicionário
                    print('-' * 20)
                    for key, values in fabricante.items():  # Varrer cada item
                        print('{}: {}'.format(key, values))
        elif consulta == '4':
            return  # Sai da função
        else:
            print('Opção inválida. Tente novamente.')
            continue  # Volta para o início do laço


def removerPeca():  # Função para remover uma peça
    codigo_desejado = int(input('Digite o código do produto que deseja remover: '))
    for peca in lista_peca:
        if peca['codigo'] == codigo_desejado:
            lista_peca.remove(peca)  # Remover a peça da lista
            print('Peça removida')


print('Bem Vindo ao controle de estoque da Bicicletaria do Wesley Kulecza')
while True:
    menu = input('Escolha a opção desejada \n'
                 '1 - Cadastrar peça\n'
                 '2 - Consultar peça\n'
                 '3 - Remover peça\n'
                 '4 - Sair\n'
                 '>> ')
    if menu == '1':
        codigo_peca += 1  # Cadastrar diferentes códigos
        cadastrarPeca(codigo_peca)  # Iniciar a função caso o usuário digite 1
    elif menu == '2':
        consultarPeca()  # Iniciar a função caso o usuário digite 2
    elif menu == '3':
        removerPeca()  # Iniciar a função caso o usuário digite 3
    elif menu == '4':
        print('Encerrando programa...')
        break  # Sair do programa
    else:
        print('Opção inválida. Tente novamente.')
        continue  # Voltar ao início do laço
