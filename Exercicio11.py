# Entrada de dados
salario_atual = float(input("Digite o salário atual do funcionário: R$ "))

# Lógica para determinar o percentual de aumento
if salario_atual <= 1000.00:
    percentual = 20
elif salario_atual <= 1700.00:
    percentual = 15
elif salario_atual <= 2300.00:
    percentual = 10
else:
    percentual = 5

# Cálculos matemáticos
# O valor do aumento é (percentual / 100) * salario
valor_aumento = salario_atual * (percentual / 100)
novo_salario = salario_atual + valor_aumento

# Exibição dos resultados formatados
print("-" * 35)
print(f"Salário digitado: R$ {salario_atual:,.2f}")
print(f"Aumento         : {percentual}%")
print(f"Valor do aumento: R$ {valor_aumento:,.2f}")
print(f"Novo salário    : R$ {novo_salario:,.2f}")
print("-" * 35)
