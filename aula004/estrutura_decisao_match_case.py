# Estrutura decisao - Match-Case

# CRUD
print('='*20, 'Modulo Usuario', '='*20, '\n')
print('\t1- Cadastrar')
print('\t2- Editar')
print('\t3- Listar')
print('\t4- Deletar')

opcao = int(input('\n\tDigite uma opcao:'))

match opcao:
    case 1:
        print('Cadastrando...')
    case 2:
        print('Editando...')
    case 3:
        print('Listando...')
    case 4:
        print('Deletando ...')
    case _:
        print('Invalido')