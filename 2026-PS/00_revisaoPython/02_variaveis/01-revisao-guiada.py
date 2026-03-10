# =================================================================
# NOME: Gabriele Bueno Martins
# DISCIPLINA: Lógica de Programação 
# DATA: 09/03/2026
# DESCRIÇÃO: Sisema de aprovação de alunos
# =================================================================


# Lista com os Alunos e suas Notas
turma = [
    {"nome": "Ana", "nota1": 8.0, "nota2": 7.5},
    {"nome": "Bruno", "nota1": 4.5, "nota2": 5.0},
    {"nome": "Caio", "nota1": 2.0, "nota2": 3.5},
    {"nome": "Caleb", "nota1": 10.0, "nota2": 10.0},
]

print("== Resultado da Turma ==\n")


# Usando "For"

for aluno in turma:
    nome  = aluno["nome"]
    nota1 = aluno["nota1"]
    nota2 = aluno["nota2"]
    media = (nota1 + nota2)/2 

# Decisão para Aprovação, Reprovação ou Reprovação


    if media>=6.0:
        situacao = "Aprovado(a)"
    elif media>=4.0:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado(a)"


# Mesagem da tela

    print(f"\n Aluno   : {nome}")
    print(f" Média   : {media}")
    print(f"Situação : {situacao}")
    print("-" *30)

continuar = "s"
while continuar == "s":
    print("\nDeseja processar outro aluno? (s/n): ", end="")
    continuar = input().lower()
    if continuar == "s":

        nome = input('Digite o nome do aluno: ')
        nota1 = float(input("\nDigite a nota 1 (0 a 10): "))
        nota2 = float(input("Digite a nota 2 (0 a 10): "))


        # Processamento

        media = (nota1 + nota2)/2 
        print(f'\nAluno   : {nome}') 
        print(f'Nota 1  : {nota1:.1f}') 
        print(f'Nota 2  : {nota2:.1f}')
        print(f'Média   : {media:.2f}\n') 
        print(f"Situação : {situacao}")

        pass