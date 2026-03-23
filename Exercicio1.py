# Entrada de dados
consumo = float(input("Digite o consumo de água em m³: "))

# Lógica de cálculo baseada nas faixas informadas
if consumo <= 10:
    valor_conta = 7.59
elif consumo <= 20:
    valor_conta = consumo * 1.31
elif consumo <= 30:
    valor_conta = consumo * 4.64
elif consumo <= 50:
    valor_conta = consumo * 6.62
else:
    valor_conta = consumo * 7.31

# Exibição do resultado formatado
print(f"O valor da conta de água é: R$ {valor_conta:.2f}")
