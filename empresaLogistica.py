print('Bem Vindo a Companhia de Logística Wesley Kulecza S.A.')


def dimensoesobjeto():  # Primeira função para calcular o volume do objeto
    try:  # Tentar usar os comandos que estão dentro do 'try'
        altu = float(input('Digite a altura do objeto (em cm): '))
        comp = float(input('Digite o comprimento do objeto (em cm): '))
        larg = float(input('Digite a largura do objeto (em cm): '))
        volume = altu * comp * larg
        if volume < 1000:  # Verificar as condições do volume de acordo com o quadro 1
            print('O volume do objeto é {} cm³.'.format(volume))
            valor = 10  # Valor em reais de acordo com o volume
            return valor  # Retornar o valor de acordo com o volume
        elif 1000 <= volume < 10000:
            print('O volume do objeto é {} cm³.'.format(volume))
            valor = 20
            return valor
        elif 10000 <= volume < 30000:
            print('O volume do objeto é {} cm³.'.format(volume))
            valor = 30
            return valor
        elif 30000 <= volume < 100000:
            print('O volume do objeto é {} cm³.'.format(volume))
            valor = 50
            return valor
        else:
            print('O volume do objeto é {} cm³.'.format(volume))
            print('Esse volume ultrapassou os limites da empresa. Tente novamente.')
            return dimensoesobjeto()
    except ValueError:  # Usado caso seja digitado algo que não foi pedido
        print('Valor inválido. Tente novamente.')
        return dimensoesobjeto()  


def pesoobjeto():  # Segunda função para calcular o multiplicador de acordo com o peso
    try:
        peso = float(input('Digite o peso do objeto (em kg): '))
        if peso < 0.1:
            print('O peso do objeto é {} kg.'.format(peso))
            mult = 1
            return mult
        elif 0.1 <= peso < 1:
            print('O peso do objeto é {} kg.'.format(peso))
            mult = 1.5
            return mult
        elif 1 <= peso < 10:
            print('O peso do objeto é {} kg.'.format(peso))
            mult = 2
            return mult
        elif 10 <= peso < 30:
            print('O peso do objeto é {} kg.'.format(peso))
            mult = 3
            return mult
        else:
            print('O peso do objeto é {} kg.'.format(peso))
            print('Esse peso ultrapassou os limites da empresa. Tente novamente.')
            return pesoobjeto()
    except ValueError:
        print('Valor inválido. Tente novamente.')
        return pesoobjeto()


def rotaobjeto():  # Terceira função para calcular o multiplicador de acordo com a rota
        print('Rotas existentes:')
        print('RS - De Rio de Janeiro até São Paulo')
        print('SR - De São Paulo até Rio de Janeiro')
        print('BS - De Brasília até São Paulo')
        print('SB - De São Paulo até Brasília')
        print('BR - De Brasília até Rio de Janeiro')
        print('RB - Rio de Janeiro até Brasília')
        rota = input('Insira a rota desejada: ')
        if rota == 'RS':
            print('Você selecionou a rota Rio de Janeiro até São Paulo.')
            mult2 = 1
            return mult2
        elif rota == 'SR':
            print('Você selecionou a rota São Paulo até Rio de Janeiro.')
            mult2 = 1
            return mult2
        elif rota == 'BS':
            print('Você selecionou a rota Brasília até São Paulo.')
            mult2 = 1.2
            return mult2
        elif rota == 'SB':
            print('Você selecionou a rota São Paulo até Brasília.')
            mult2 = 1.2
            return mult2
        elif rota == 'BR':
            print('Você selecionou a rota Brasília até Rio de Janeiro.')
            mult2 = 1.5
            return mult2
        elif rota == 'RB':
            print('Você selecionou a rota Rio de Janeiro até Brasília.')
            mult2 = 1.5
            return mult2
        else:
            print('Essa opção de rota não existe. Tente novamente.')
            return rotaobjeto()


dimensoes = dimensoesobjeto()
peso = pesoobjeto()
rota = rotaobjeto()
total = dimensoes * peso * rota  # Cálculo do valor total
print('O valor total a ser pago é R${}.'.format(total))
