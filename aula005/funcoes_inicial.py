def saudacao(nome): # nome é um parâmetro
    print('Olá,', nome)

# responsabilidade única
def soma(n1, n2): # tem dois parâmentros = n1 e n2
    resultado = n1 + n2
    return resultado


saudacao('João') # argumento "Jaoa"
saudacao('Maria') # argumento "Maria"

resultado = 0
for n in range(10, -1, -1):
    resultado += soma(n, n-1)

print(resultado)




