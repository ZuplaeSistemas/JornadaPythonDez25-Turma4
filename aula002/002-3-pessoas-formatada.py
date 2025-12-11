print('='*20, 'Cadastro de Funcionarios', '='*20, '\n')

print('\t', 'Nome:', 'Joao')
print('\t', 'Sobrenome:', 'Silva')
print('\t', 'Idade:', 89)
print('\t', 'Salario:', 2975.40)
print('\t', 'Ativo:', True)

print('='*23, 'Final do Programa', '='*23)
# funcao format
print('{}{} {} {}'.format('\n', '='*23, 'Final do Programa', '='*23))
# f-strings - interpolacao de strings
print(f'{'\n'}{'='*23} {'Final do Programa'} {'='*23}')