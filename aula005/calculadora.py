from calculo import (
    soma, 
    subtracao,
    multiplicacao, 
    divisao
)


numero1 = float(input('Digite o primeiro numero: '))
numero2 = float(input('Digite o segundo numero: '))

print('soma:', soma(numero1, numero2))
print('subtração:',subtracao(numero1, numero2))
print('multiplicação:',multiplicacao(numero1, numero2))
print('divisão:',divisao(numero1, numero2))
