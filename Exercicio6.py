# Entrada de dados
a = float(input("Digite o lado A: "))
b = float(input("Digite o lado B: "))
c = float(input("Digite o lado C: "))

# 1. Verificação da existência do triângulo
# A soma de dois lados deve ser sempre maior que o terceiro
if (a + b > c) and (a + c > b) and (b + c > a):
    print("Os valores formam um triângulo!")
    
    # 2. Classificação do triângulo
    if a == b == c:
        print("Tipo: Equilátero (Todos os lados iguais)")
    elif a == b or a == c or b == c:
        print("Tipo: Isósceles (Dois lados iguais)")
    else:
        print("Tipo: Escaleno (Todos os lados diferentes)")
else:
    print("Opção inválida! Os valores informados não podem formar um triângulo.")
