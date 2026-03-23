# 1. Entrada das quatro notas bimestrais
nota1 = float(input("Digite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))
nota3 = float(input("Digite a 3ª nota: "))
nota4 = float(input("Digite a 4ª nota: "))

# 2. Cálculo da média final
media = (nota1 + nota2 + nota3 + nota4) / 4

# 3. Definição do Conceito baseado na média
if 9.0 <= media <= 10.0:
    conceito = "A"
elif 7.5 <= media < 9.0:
    conceito = "B"
elif 6.0 <= media < 7.5:
    conceito = "C"
elif 4.0 <= media < 6.0:
    conceito = "D"
else:
    conceito = "E"

# 4. Definição da situação (APROVADO ou REPROVADO)
if conceito in ["A", "B", "C"]:
    situacao = "APROVADO"
else:
    situacao = "REPROVADO"

# --- EXIBIÇÃO DOS RESULTADOS ---
print("\n" + "="*30)
print(f"NOTAS: {nota1} | {nota2} | {nota3} | {nota4}")
print(f"MÉDIA FINAL: {media:.1f}")
print(f"CONCEITO: {conceito}")
print("-" * 30)
print(f"SITUAÇÃO: {situacao}")
print("="*30)
