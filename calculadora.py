# CÓDIGO DE CALCULADORA

num1 = 0
num2 = 0
result = 0
op  = ' '

while True:
    num1 = int(input('Digite um número:')) #ler o primeiro numero

    op = input('Digite a operação matemática')
    num2 = int(input('Digite outro número:'))

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        result = num1 / num2
    else:
        print('Operação não reconhecida!')

    print('{} {} {} = {}'.format(num1, op, num2, result))
