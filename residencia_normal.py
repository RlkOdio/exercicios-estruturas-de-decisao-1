# residencia_normal.py

# Entrada do consumo
consumo = float(input("Digite o consumo de água da residência normal (m³): "))

# Lógica de cálculo conforme as novas faixas
if consumo <= 10:
    valor_conta = 22.38
elif consumo <= 20:
    valor_conta = consumo * 3.50
elif consumo <= 50:
    valor_conta = consumo * 8.75
else:
    valor_conta = consumo * 9.64

# Exibição do resultado
print(f"O valor da conta para residência normal é: R$ {valor_conta:.2f}")
