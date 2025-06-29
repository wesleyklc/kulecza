print('Bem vindo a lanchonete do Wesley Kulecza!')
print('****************CARDÁPIO*****************')
print('| CÓDIGO |        DESCRIÇÃO      | VALOR |')
print('|   100  |    Cachorro Quente    |  9,00 |')
print('|   101  | Cachorro Quente Duplo | 11,00 |')
print('|   102  |         X-Egg         | 12,00 |')
print('|   103  |        X-Salada       | 12,00 |')
print('|   104  |         X-Bacon       | 14,00 |')
print('|   105  |         X-Tudo        | 17,00 |')
print('|   200  |   Refrigerante Lata   |  5,00 |')
print('|   201  |       Chá Gelado      |  4,00 |')

total = 0  # Valor total a ser pago pelo cliente
while True:  # O número de pedido do cliente não é conhecido, logo foi usado o while
    cod = input('Entre com o código desejado: ')
    if cod == '100' or '101' or '102' or '103' or '104' or '105' or '200' or '201':
        if cod == '100':
            x = 9
            print('Você escolheu um cachorro-quente no valor de R${},00.'.format(x))
            total += x  # Código para somar os valores dos pedidos
        elif cod == '101':
            x = 11
            print('Você escolheu um cachorro-quente duplo no valor de R${},00.'.format(x))
            total += x
        elif cod == '102':
            x = 12
            print('Você escolheu um x-egg no valor de R${},00.'.format(x))
            total += x
        elif cod == '103':
            x = 12
            print('Você escolheu um x-salada no valor de R${},00.'.format(x))
            total += x
        elif cod == '104':
            x = 14
            print('Você escolheu um x-bacon no valor de R${},00.'.format(x))
            total += x
        elif cod == '105':
            x = 17
            print('Você escolheu um x-tudo no valor de R${},00.'.format(x))
            total += x
        elif cod == '200':
            x = 5
            print('Você escolheu um refriferante lata no valor de R${},00.'.format(x))
            total += x
        elif cod == '201':
            x = 4
            print('Você escolheu um chá gelado no valor de R${},00.'.format(x))
            total += x
        else:
            print('Código inválido.')  # Qualquer código diferente dos apresentados no primeiro "if" é dado como inválido, voltando a operação no início
            continue                   
        print('Deseja pedir mais alguma coisa? ')
        print('1 - SIM')
        print('2 - NÃo')
    x = input('>> ')
    if x == '1':
        continue   # Caso o cliente digite "1", a operação retorna ao início
    elif x == '2':
        break  # Caso o cliente digite "2", a operação termina e o valor final é apresentado a ele
print('O valor total é R${},00.'.format(total))


