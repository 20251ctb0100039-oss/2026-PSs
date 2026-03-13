# =================================================================
# NOME: Gabriele Bueno Martins
# DISCIPLINA: Lógica de Programação 
# DATA: 09/03/2026
# DESCRIÇÃO: Sistema de Catalogo de Livros
# =================================================================

#lista

catalogo =[
    {"titulo": "Ainda Estou Aqui", "autor": "Rubens Paiva", "ano": 2015, "disponivel": True},
    {"titulo": "A revolução dos Bichos", "autor": "George Orwell", "ano": 1945, "disponivel": False},
    {"titulo": "O alquimista", "autor": "Paulo Coelho", "ano": 1988, "disponivel": True},
    {"titulo": "A Hipótese do Amor", "autor": " Ali Hazelwood", "ano": 2022, "disponivel": True},
]
#pra mostrar o catálogo
for i, livro in enumerate(catalogo, start=1):
    status = "Disponivel" if livro ["disponivel"] else "Emprestado"
    print(f"\n{i}  {livro['titulo']} ({livro["ano"]})")
    print(f"  Autor:  {livro['autor']} | {status}")
    print("  "+ "-" *40)

opcao = input("\nDeseja procurar um autor e seus livros? (s/n)").lower()
if opcao == "s":
    print("\n**** Busca por Autor ****")
    busca = input("Digite o nome do autor (ou parte): ").lower()
    encontrado = False
    for livro in catalogo:
        if busca in livro["autor"].lower():
            print(f'Encontrado: {livro["titulo"]} - {livro["autor"]}')
            encontrado = True
    if not encontrado:
        print ("Nenhum autor encontrado com esse nome.")

opcaoB = input("\nDeseja adicionar um livro novo? (s/n)").lower()
if opcaoB =="s":
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = int(input("Ano: "))
    Disponivel = input("Disponível? (s/n)").lower()
    if Disponivel == "s":
        DisponivelV = True
    else:DisponivelV = False
    livro_novo = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "disponivel": DisponivelV
    }
    catalogo.append(livro_novo)
    print("\n Livro novo adicionado")
    for i, livro in enumerate(catalogo, start=1):
        status = "Disponível" if livro["disponivel"] else "Emprestado"
        print(f"\n{i} - {livro['titulo']} ({livro['ano']})")
        print(f"  Autor: {livro['autor']} | {status}")
        print("  " + "=" * 40)

print("\n Livros Emprestados:")
emprestados = False
for livro in catalogo:
    if not livro["disponivel"]:
        print(f"- {livro['titulo']}")
        emprestados = True
if not emprestados:
    print("Nenhum livro está emprestado no momento.")
