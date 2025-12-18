from time import sleep

nomes = ['Joao', 'Maria', 'Jose', 'Joana']

numero = 0
while numero < 10:
    print(numero)
    numero = numero + 1 # incremento

index = 0
while index < len(nomes):
    print(nomes[index])
    index += 1

opcao = -1
while opcao != 0:
    print('='*20, 'Modulo Usuario', '='*20, '\n')
    print('\t1- Cadastrar')
    print('\t2- Editar')
    print('\t3- Listar')
    print('\t4- Deletar')
    print('\t0- Sair')

    opcao = int(input('\n\tDigite uma opcao:'))

    match opcao:
        case 0:
            print('Saindo ...')
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
    sleep(2)