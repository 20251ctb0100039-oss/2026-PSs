# =============================================================================
# INSTITUTO FEDERAL DO PARANÁ - IFPR
# CURSO: informática
# DISCIPLINA: Programação
# ESTUDANTE: Gabriele Bueno Martins
# DATA: 05/03/2026
# DESCRIÇÃO: Sistema de Gestão de Notas Modularizado 
# =============================================================================

#DEFINIÇÃO DE FUNÇÕES

def calcular_media(n1, n2):
    """Retorna a média aritmética simples entre duas notas."""
    return (n1 + n2) / 2

def verificar_situacao(media):
    """Define o status do aluno com base nos critérios do IFPR."""
    if media >= 6.0:
        return "Aprovado"
    elif 4.0 <= media < 6.0:
        return "Recuperação"
    else:
        return "Reprovado"

def solicitar_notas(nome_aluno):
    """Solicita e valida duas notas entre 0 e 10 para um aluno específico."""
    notas = []
    i = 1
    print(f"\n--- Coletando notas de: {nome_aluno} ---")
    while len(notas) < 2:
        try:
            nota = float(input(f"Digite a {i}ª nota (0-10): "))
            if 0 <= nota <= 10:
                notas.append(nota)
                i += 1
            else:
                print("⚠️ Erro: A nota deve estar entre 0 e 10.")
        except ValueError:
            print("⚠️ Erro: Digite um valor numérico válido.")
    return notas[0], notas[1]

def gerar_relatorio(nome, media, situacao):
    """Exibe o boletim individual formatado."""
    print("-" * 30)
    print(f"ALUNO: {nome}")
    print(f"MÉDIA: {media:.1f}")
    print(f"SITUAÇÃO: {situacao}")
    print("-" * 30)

def calcular_media_turma(medias):
    """Calcula a média geral da turma usando recursão."""
    if not medias:
        return 0
    if len(medias) == 1:
        return medias[0]
    
    # Lógica recursiva: (primeiro item + soma do restante) / n ao final
    # Para facilitar a recursão pura sem sum(), somamos os itens e dividimos no final
    def soma_recursiva(lista):
        if not lista: return 0
        return lista[0] + soma_recursiva(lista[1:])
    
    return soma_recursiva(medias) / len(medias)

def resumo_turma(dados_alunos):
    """Conta aprovados, recuperação e reprovados."""
    aprovados = 0
    recuperacao = 0
    reprovados = 0
    
    for aluno in dados_alunos:
        situacao = aluno['situacao']
        if situacao == "Aprovado":
            aprovados += 1
        elif situacao == "Recuperação":
            recuperacao += 1
        else:
            reprovados += 1
            
    return aprovados, recuperacao, reprovados


#PROGRAMA PRINCIPAL

def main():
    turma = []
    lista_medias = []
    quantidade_alunos = 3

    print("=== SISTEMA PEDAGÓGICO IFPR ===")

    for _ in range(quantidade_alunos):
        nome = input("\nNome do aluno: ")
        nota1, nota2 = solicitar_notas(nome)
        
        media = calcular_media(nota1, nota2)
        situacao = verificar_situacao(media)
        
        # Armazena dados para o resumo final
        turma.append({'nome': nome, 'situacao': situacao})
        lista_medias.append(media)
        
        # Relatório individual imediato
        gerar_relatorio(nome, media, situacao)

    # Processamento Final (Avançado)
    media_geral = calcular_media_turma(lista_medias)
    aprov, rec, reprov = resumo_turma(turma)

    print("\n" + "="*40)
    print("📊 RESUMO FINAL DA TURMA")
    print(f"Média Geral da Turma: {media_geral:.2f}")
    print(f"Total de Aprovados:    {aprov}")
    print(f"Total em Recuperação:  {rec}")
    print(f"Total de Reprovados:   {reprov}")
    print("="*40)

if __name__ == "__main__":
    main()