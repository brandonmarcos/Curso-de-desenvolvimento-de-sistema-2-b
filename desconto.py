preco = float(input("Digite um número: "))
desconto = float(input("Digite outro número: "))
valordesconto = preco * desconto/100
precofinal = preco - valordesconto

print("Valor do desconto: ", valordesconto)
print("Valor final: ", precofinal)    