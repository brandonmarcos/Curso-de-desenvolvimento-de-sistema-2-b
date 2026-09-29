n1 = float(input("Digite seu número: "))
n2 = float(input("Digite outro número: "))
n3 = input("Digite a operação (+, -, / ou *): ")

if n3 == "+":
    resultado = n1 + n2
elif n3 == "-":
    resultado = n1 - n2
elif n3 == "/":
    resultado = n1 / n2
elif n3 == "*":
    resultado = n1 * n2
else:
    resultado = "Operação inválida!"

print(resultado)