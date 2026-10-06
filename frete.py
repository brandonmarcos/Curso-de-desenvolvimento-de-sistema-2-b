valor = float(input("Digite o valor da compra: "))

if valor >= 200:
    frete = 0
elif valor >= 100:
    frete = 10
else:
    frete = 20

total = valor + frete

print("Frete:", frete)
print("Total:", total)