# Entrada de dados
turno = input("Em que turno você estuda? (M-Matutino, V-Vespertino, N-Noturno): ")

# Estrutura de decisão
if turno == 'M':
    print("Bom Dia!")
elif turno == 'V':
    print("Boa Tarde!")
elif turno == 'N':
    print("Boa Noite!")
else:
    print("Valor Inválido!")
