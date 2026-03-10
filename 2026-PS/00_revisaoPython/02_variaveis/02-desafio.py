# =================================================================
# NOME: Gabriele Bueno Martins
# DISCIPLINA: Lógica de Programação 
# DATA: 09/03/2026
# DESCRIÇÃO: Sistema de Gerenciamento de Estoque
# =================================================================

# Lista do estoque
estoque = [
    {"nome": "Mouse Gamer", "qtd": 4},
    {"nome": "Teclado Mecânico", "qtd": 15},
    {"nome": "Monitor 24'", "qtd": 25}
]

# Inicialização de contadores para o relatório final
criticos = 0     
adequados = 0   
excessos = 0   

print("=== Bem-vindo ao Sistema de Estoque v1.0 ===")

# cadastro de vários produtos
while True:
    # Pergunta ao usuário se ele quer continuar
    adicionar = input("\nDeseja cadastrar um novo produto? (s/n): ").lower()
    
    # se o usuário digitar qualquer coisa diferente de 's', o loop quebra
    if adicionar != 's':
        break
    
    nome_novo = input("Nome do produto: ")
    
    # quantidade precisa um número válido
    while True:
        try:
            # Converte a entrada de texto para número inteiro
            qtd_nova = int(input(f"Quantidade de {nome_novo}: "))
            
            # Impede a entrada de números negativos
            if qtd_nova < 0:
                print("Erro: A quantidade não pode ser negativa.")
                continue
            break 
        except ValueError:
            # se for letra 
            print("Erro: Por favor, digite um número inteiro válido.")
    
    # para adicionar um novo produto 
    estoque.append({"nome": nome_novo, "qtd": qtd_nova})
    print(f"✅ {nome_novo} adicionado com sucesso!")

# Geração do Relatório
print("\n" + "="*40)
# Cabeçalho formatado com alinhamento à esquerda (<) para criar colunas
print(f"{'PRODUTO':<20} | {'QTD':<5} | {'SITUAÇÃO'}")
print("-" * 40)

# Define o primeiro item da lista como referência inicial pra comparar o menor estoque
produto_mais_critico = estoque[0]

# cada item da lista de estoque para classificar e imprimir
for item in estoque:
    nome = item["nome"]
    qtd = item["qtd"]
    
    # Estrutura condicional para definir a categoria do estoque
    if qtd < 5:
        situacao = "CRÍTICO"
        criticos += 1 
    elif 5 <= qtd <= 20:
        situacao = "ADEQUADO"
        adequados += 1
    else:
        situacao = "EXCESSO"
        excessos += 1
    
    # para encontrar o item com a menor quantidade absoluta
    if qtd < produto_mais_critico["qtd"]:
        produto_mais_critico = item

    # linha do produto formatada em colunas
    print(f"{nome:<20} | {qtd:<5} | {situacao}")

# resumo quantitativo e o alerta do item mais baixo
print("-" * 40)
print(f"RESUMO: {criticos} Críticos | {adequados} Adequados | {excessos} Excessos")
print(f"ALERTA: O item mais crítico é '{produto_mais_critico['nome']}' com apenas {produto_mais_critico['qtd']} unidades.")
print("="*40)


while True:
    # remove espaços em branco acidentais no início ou fim da digitação
    busca = input("\nDigite o nome de um produto para consultar (ou 'sair'): ").strip()
    
    if busca.lower() == 'sair':
        break
    
    achado = False # Flag para controlar se o produto foi localizado
    for item in estoque:
        
        if item["nome"].lower() == busca.lower():
            print(f"-> Resultado: {item['nome']} possui {item['qtd']} unidades em estoque.")
            achado = True
            break 
    
    # Se percorrer toda a lista e a flag continuar 'False', informa erro
    if not achado:
        print(f"⚠️ Produto '{busca}' não encontrado no sistema.")

print("\nSistema encerrado. Bom trabalho!")