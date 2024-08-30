# desafio 1

from time import sleep

def titulo():
    msg = 'Sequência de Fibonacci'
    print('-' * len(msg))
    print(msg)
    print('-' * len(msg))

def inputNumber():

    while True:
        
        numero = input('digite um número: ')

        # verificar se o numero é valido e convertendo para int
        
        if numero.isdigit():
            numero = int(numero)
            break
        
        else:
            print('valor inválido!')
    
    return numero

# a funcao gera a sequencia até o numero dado e verifica se o numero pertence ou nao a ela
def sequenciaFibonacci(number):

    # inicializar termos
    a = 0
    b = 1
    sequencia = [a]

    # faz a sequencia ate que o proximo termo seja maior ou igual a 'number'
    
    while b <= number:
        sequencia.append(b)
        a, b = b, a + b

    print("Calculando sequência...")
    sleep(2)
    print(sequencia, '...')

    # verificar se o numero pertence a sequencia de fibonacci
    if number in sequencia:
        return f"O número {number} pertence à sequência de Fibonacci!"
    else:
        return f"O número {number} não pertence à sequência de Fibonacci!"

def main():
    titulo()
    while True:
        num = inputNumber()
        print(sequenciaFibonacci(num))
        opcao = input('quer digitar outro número? [1 - sim, 2 - não] ')
        if opcao == '2':
            print('até logo!')
            break

if __name__ == "__main__":
    main()