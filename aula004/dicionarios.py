#estrutura de dadas - Dicionario = JSON

# Funcionario
nome = 'Joao'
sobrenome = 'Silva'
idade = 15
salario = 1999.99
ativo = True

# chave-valor
funcionario = {
    'nome':'Joao'
    ,'sobrenome':'Silva'
    ,'idade':15
    ,'salario':1999.99
    ,'ativo': True
}

print(funcionario)
print( funcionario['nome'])
print( funcionario.get('nome') )

funcionario['nome'] = 'Maria'
print(funcionario)

del funcionario['ativo']
print(funcionario)

funcionario['endereco'] = 'Rua 1, n0'
print(funcionario)