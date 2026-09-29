capital = float(input("Digite o capital investido: "))
taxa = float(input("Digite a taxa de juros: "))
tempo = float(input("Digite o tempo de investimento: "))

juros = capital * taxa * tempo
montante = capital + juros

print("Juros:", juros)
print("Montante:", montante)