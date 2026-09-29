nota1 = float(input("Digite o valor da nota1: "))
nota2 = float(input("Digite o valor da nota2: "))
nota3 = float(input("Digite o valor da nota3: "))
nota4 = float(input("Digite o valor da nota4: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print("O valor da nota1, nota2, nota3 e nota4:", media)

if media >= 5:
    print("Aluno Aprovado!")
else:
    print("Aluno Reprovado!")