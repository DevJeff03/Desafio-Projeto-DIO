def soma():
    num1 = input('Digite um numero para fazer a soma: ')
    num2 = input('digite o segundo numero: ')
    print()

    while not num1.isnumeric() or not num2.isnumeric():
        print('Favor digitar dois números: ')
        num1 = input('Digite um numero para fazer a soma: ')
        num2 = input('digite o segundo numero: ')
        print()
    num1 = int(num1)
    num2 = int(num2)
    print(f'{num1} + {num2}  = {num1 + num2}')


def sub():
    num3 = input('Digite um numero para fazer a subtração: ')
    num4 = input('digite o segundo numero: ')
    print()

    while not num3.isnumeric() or not num4.isnumeric():
        print('Favor digitar dois números: ')
        num3 = input('Digite um numero para fazer a subtração: ')
        num4 = input('digite o segundo numero: ')
        print()
    num3 = int(num3)
    num4 = int(num4)
    print(f'{num3} - {num4}  = {num3 - num4}')


def multp():
    print('Gostaria de fazer uma multiplicação entre dois numeros ou uma tabuada?')
    opcao = input('1 - Tabuada / 2 - Multip. Especifica : ')

    if opcao.isnumeric():
        if opcao == '1':
            numx = input('Qual numero gostaria de saber a tabuada? ')
            numx = int(numx)
            for contador in range(1, 11):
                print(f'{numx} * {contador} = {numx * contador}')
        if opcao == '2':
            num5 = input('Digite um numero para fazer a Multiplicação: ')
            num6 = input('digite o segundo numero: ')
            print()

            while not num5.isnumeric() or not num6.isnumeric():
                print('Favor digitar dois números: ')
                num5 = input('Digite um numero para fazer a Multiplicação: ')
                num6 = input('digite o segundo numero: ')
                print()
            num5 = int(num5)
            num6 = int(num6)
            print(f'{num5} x {num6}  = {num5 * num6}')
    else:
        print('Opção inválida!')


def divisão():
    num7 = input('Digite um numero para fazer a divisão: ')
    num8 = input('digite o segundo numero: ')
    print()

    while not num7.isnumeric() or not num8.isnumeric():
        print('Favor digitar dois números: ')
        num7 = input('Digite um numero para fazer a divisão: ')
        num8 = input('digite o segundo numero: ')
        print()
    num7 = int(num7)
    num8 = int(num8)
    print(f'{num7} / {num8}  = {num7 / num8:.2f}')


continuar = 'Y'

while continuar == 'Y':

    print()
    print('***************   Cauculadora Digital   ***************')
    print()
    print('****   Qual operação você gostaria de executar?   ****')
    print()
    escolha = input('1 - Soma - 2 - Subtração - 3 - Multiplicação - 4 - Divisão : ')
    print()
    escolha = int(escolha)

    if escolha == 1:
        soma()
    elif escolha == 2:
        sub()
    elif escolha == 3:
        multp()
    elif escolha == 4:
        divisão()
    else:
        print('Escolha uma opção válida!')
    print()
    continuar = input('Deseja continuar? Y/N : ')
    if continuar == 'y':
        continuar = 'Y'
print()
print('Fim do Programa!!!')
