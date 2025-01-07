def soma(num1,num2):
    resultado = num1 + num2
    return resultado
def subtracao(num1,num2):
    resultado = num1 - num2
    return resultado
def divisao(num1,num2):
    if num2 == 0:
        return 'Não é possivel fazer uma divisão por 0'
    resultado = num1 / num2
    return resultado
def multiplicacao(num1,num2):
    resultado = num1 * num2
    return resultado

def pegaNumeros():
    numero1 = float(input("Digite o primeiro numero: "))
    numero2 = float(input("Digite o segundo numero: "))
    return numero1, numero2

    

contador = 1
while contador > 0:
    print('-------------------------------------------')
    print('                Calculadora           ')
    print('-------------------------------------------')
    print('1- Soma')
    print('2- Subtração')
    print('3- Divisão')
    print('4- multiplicação')
    print(f'5- Sair da calculadora!!!\n')
    entrada = int(input("Qual conta deseja fazer?"))

    
    if entrada == 1:
        numero1, numero2 =  pegaNumeros()
        print(f'\n\nA soma entre {numero1} e {numero2} é {soma(numero1,numero2)}')
    elif entrada == 2:
        numero1, numero2 =  pegaNumeros()
        print(f'\n\nA Subtração entre {numero1} e {numero2} é {subtracao(numero1,numero2)}')
    elif entrada == 3:
        numero1, numero2 =  pegaNumeros() 
        print(f'\n\nA Divisão entre {numero1} e {numero2} é {divisao(numero1,numero2)}')
    elif entrada == 4:
        numero1, numero2 =  pegaNumeros()
        print(f'\n\nA Multiplicação entre {numero1} e {numero2} é {multiplicacao(numero1,numero2)}')
    elif entrada == 5:
        contador = -1
    else:
        print('Erro: digite um valor valido para "Qual conta deseja fazer?"')
    
   
