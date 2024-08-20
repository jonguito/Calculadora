print('+='*40)
print('CALCULADORA DO JÃO!!! (:')
print('+='*40)
while True:
    operacao = int(input('''digite qual operação deseja fazer
1 - adição(+)
2 - subtração(-)
3 - divisão(/)
4 - multiplicação(*)
5 - sair
                     '''))
    if operacao == 1:
        adicao1 = float(input('Digite o primeiro valor que deseja fazer a adição:'))
        adicao2 = float(input('Digite o segundo valor que deseja fazer a adição: '))
        result_1 = int(adicao1 + adicao2) 
        print(f'{adicao1} + {adicao2} = {result_1}')
        print('+='*40)
        
    elif operacao == 2:
        subtracao1 = float(input('Digite o primeiro valor que deseja fazer a subtração: '))
        subtracao2 = float(input('Digite o segundo valor que deseja fazer a subtração: '))
        result_2 = int(subtracao1 - subtracao2)
        print(f'{subtracao1} - {subtracao2} = {result_2}') 
        print('+='*40)
        
    elif operacao == 3:
        divisao1 = float(input('Digite o primeiro valor que deseja dividir: '))
        divisao2 = float(input('Digite o segundo valor que deseja dividir: '))
        result3 = int(divisao1 / divisao2)
        print (f'{divisao1} / {divisao2} = {result3}') 
        print('+='*40)
        
    elif operacao == 4:
        multiplicacao1 = float(input('Digite o primeiro valor que deseja multiplicar: '))
        multiplicacao2 = float(input('Digite o segundo valor que deseja multiplicar: '))
        result4 = int(multiplicacao1 * multiplicacao2)
        print(f'{multiplicacao1} * {multiplicacao2} = {result4}')
        print('+='*40)
        
    if operacao == 5:
        print('+='*40)
        print('OBRIGADO E ATÉ MAIS (: ')
        print('+='*40)
        break
