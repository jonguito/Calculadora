print('+='*40)
print('CALCULADORA DO JÃO!!! (:')
print('+='*40)
while True:
    operaçao = int(input('''digite qual operação deseja fazer
1 - adição(+)
2 - subtração(-)
3 - divisão(/)
4 - multiplicação(*)
5 - sair
                     '''))
    if operaçao == 1:
        adiçao1 = float(input('Digite o primeiro valor que deseja fazer a adição:'))
        adiçao2 = float(input('Digite o segundo valor que deseja fazer a adição: '))
        result_1 = int(adiçao1 + adiçao2) 
        print(f'''{adiçao1} + {adiçao2} = {result_1}
===============================================================''')   
    if operaçao == 2:
        subtraçao1 = float(input('Digite o primeiro valor que deseja fazer a subtração: '))
        subtraçao2 = float(input('Digite o segundo valor que deseja fazer a subtração: '))
        result_2 = int(subtraçao1 - subtraçao2)
        print(f'''{subtraçao1} - {subtraçao2} = {result_2}
===============================================================''') 
    if operaçao == 3:
        divisao1 = float(input('Digite o primeiro valor que deseja dividir: '))
        divisao2 = float(input('Digite o segundo valor que deseja dividir: '))
        result3 = int(divisao1 / divisao2)
        print (f'''{divisao1} / {divisao2} = {result3}
===============================================================''')   
    if operaçao == 4:
        multiplicaçao1 = float(input('Digite o primeiro valor que deseja multiplicar: '))
        multiplicaçao2 = float(input('Digite o segundo valor que deseja multiplicar: '))
        result4 = int(multiplicaçao1 * multiplicaçao2)
        print(f'''{multiplicaçao1} * {multiplicaçao2} = {result4}
===============================================================''')
    if operaçao == 5:
        print('+='*40)
        print('OBRIGADO E ATÉ MAIS (: ')
        print('+='*40)
        break
