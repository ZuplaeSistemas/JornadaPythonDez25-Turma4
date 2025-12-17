# Estruturas de dados

nomes = ['Joao', 'Maria', 'Jose']
numeros = [10, 52, 41, 67]

print(nomes)
print(numeros)

print(nomes[1]) # indice - index
print(numeros[2])

print(nomes[-1]) # ordem reversa

print( len(nomes) ) # quantidade de elementos
print( len(numeros) )

nomes.append('Joana')
print(nomes)

nomes[1] = 'Marta'
print(nomes)

nomes.remove('Jose')
print(nomes)

nome_removido = nomes.pop(0)
print(nomes)
print(nome_removido)