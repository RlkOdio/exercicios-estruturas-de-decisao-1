# Entrada do salário bruto
salario_bruto = float(input("Digite o valor do salário bruto (R$): "))

# --- CÁLCULO DO INSS (Simplificado para fins didáticos) ---
# Em um sistema real, o cálculo é progressivo por faixa.
if salario_bruto <= 1412.00:
    aliquota_inss = 0.075
elif salario_bruto <= 2666.68:
    aliquota_inss = 0.09
elif salario_bruto <= 4000.03:
    aliquota_inss = 0.12
else:
    aliquota_inss = 0.14

desconto_inss = salario_bruto * aliquota_inss

# O IRRF é calculado sobre o (Salário Bruto - INSS)
base_irrf = salario_bruto - desconto_inss

# --- CÁLCULO DO IRRF (Simplificado) ---
if base_irrf <= 2259.20:
    aliquota_irrf = 0
    deducao = 0
elif base_irrf <= 2826.65:
    aliquota_irrf = 0.075
    deducao = 169.44
elif base_irrf <= 3751.05:
    aliquota_irrf = 0.15
    deducao = 381.44
elif base_irrf <= 4664.68:
    aliquota_irrf = 0.225
    deducao = 662.77
else:
    aliquota_irrf = 0.275
    deducao = 896.00

desconto_irrf = (base_irrf * aliquota_irrf) - deducao

# Resultados
salario_liquido = salario_bruto - desconto_inss - desconto_irrf

print("-" * 30)
print(f"Salário Bruto:   R$ {salario_bruto:8.2f}")
print(f"Desconto INSS:   R$ {desconto_inss:8.2f}")
print(f"Desconto IRRF:   R$ {desconto_irrf:8.2f}")
print("-" * 30)
print
