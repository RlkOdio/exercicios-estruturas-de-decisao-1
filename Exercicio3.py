# comercial_industrial.py

# Entrada do consumo
consumo = float(input("Digite o consumo de água (comercial/industrial) em m³: "))

# Lógica de cálculo para categoria Comercial/Industrial
if consumo <= 10:
    valor_conta = 44.95
elif consumo <= 20:
    valor_conta = consumo * 8.75
elif consumo <= 50:
    valor_conta = consumo * 16.76
else:
    valor_conta = consumo * 17.46

# Exibição do resultado
print("-" * 30)
print(f"CATEGORIA: COMERCIAL/INDUSTRIAL")
print(f"VALOR DA CONTA: R$ {valor_conta:.2f}")
print("-" * 30)
