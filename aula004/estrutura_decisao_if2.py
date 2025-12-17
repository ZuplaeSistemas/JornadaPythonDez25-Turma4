nota = 4

# maior ou igual a 9 = "Excelente"
# acima de 7 = "Aprovado"
# acima de 5 = "Recuperacao"
# abaixo de 5 = "Reprovado"

if nota >= 9:
    print('Excelente')
else:
    if nota >= 7:
        print('Aprovado')
    else:
        if nota >= 5:
            print('Recuperacao')
        else:
            print('Reprovado')

if nota >= 9:
    print('Excelente')
elif nota >= 7:
    print('Aprovado')
elif nota >= 5:
    print('Recuperacao')
else:
    print('Reprovado')

