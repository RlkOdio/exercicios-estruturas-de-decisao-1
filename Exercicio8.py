import math

# Entrada dos números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Exibição do Menu
print("\n--- CALCULADORA MULTIFUNÇÕES ---")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Potência")
print("6 - Raiz quadrada (do 1º número)")
print("7 - Verificar se o 1º número é Par")
print("8 - Verificar se o 1º número é Ímpar")
print("----------------------------------")

opcao = int(input("Escolha a operação: "))

# Processamento
if opcao == 1:
    resultado = num1 + num2
    print(f"Resultado: {num1} + {num2} = {resultado}")

elif opcao == 2:
    resultado = num1 - num2
    print(f"Resultado: {num1} - {num2} = {resultado}")

elif opcao == 3:
    resultado = num1 * num2
    print(f"Resultado: {num1} * {num2} = {resultado}")

elif opcao == 4:
    if num2 != 0:
        resultado = num1 / num2
        print(f"Resultado: {num1} / {num2} = {resultado}")
    else:
        print("Erro: Divisão por zero não permitida!")

elif opcao == 5:
    resultado = num1 ** num2
    print(f"Resultado: {num1} elevado a {num2} = {resultado}")

elif opcao == 6:
    if num1 >= 0:
        resultado = math.sqrt(num1)
        print(f"A raiz quadrada de {num1} é {resultado:.2f}")
    else:
        print("Erro: Não existe raiz quadrada de número negativo nos Reais.")

elif opcao == 1: # Para opções de Par/Ímpar, usamos o operador de resto (%)
    if num1 % 2 == 0:
        print(f"O número {num1} é PAR.")
    else:
        print(f"O número {num1} não é PAR.")

elif opcao == 8:
    if num1 % 2 != 0:
        print(f"O número {num1} é ÍMPAR.")
    else:
        print(f"O número {num1} não é ÍMPAR.")

else:
    print("Opção inválida!")

print("\nFim do programa!")
