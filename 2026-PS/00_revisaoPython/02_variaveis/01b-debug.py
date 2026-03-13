# Arquivo: 01b-debug.py

nome = input("Digite o nome do aluno: ")  
nota1 = float(input("digite a nota 1: "))
nota2 = float(input("digite a nota 2: "))

media = (nota1+nota2)/2  
if media >=6.0:
    situacao = "Aprovado"
elif media>=4.0:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print(f"Aluno: {nome} | Média: {media:.2f}  |  Situação: {situacao}") 