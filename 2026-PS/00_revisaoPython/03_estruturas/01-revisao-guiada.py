# =================================================================
# NOME: Gabriele Bueno Martins
# DISCIPLINA: Lógica de Programação 
# DATA: 09/03/2026
# DESCRIÇÃO: Sisema de Biblioteca
# =================================================================


# Lista de Títulos
titulos =[
    "O Programador Pragmático",
    "Código Limpo",
    "Entendendo Algoritimos",
]

# Acesso por Índice(começa em 0)
print("Primeiro Livro:", titulos[0])
print("Último Livro:", titulos[-1])
print("Total de Livros:", len(titulos))


# Métodos de Lista

print("\n--- Operações na Lista ---")

#Adicionar um item ao final
titulos.append("Python Fluente")
print("Após append:", titulos)

#Verificar se um item existe
busca= "Código Limpo"
if busca in titulos:
    print (f'"{busca}" está no catálogo.')
else:
    print(f'"{busca}" não encontrado.')


for i, titulos in enumerate(titulos, start=1):
    print(f"{i}: {titulos}")

print("\n \n \n \n")


# Dicionario: conceitos basicos

# livro com os atributos
livro = {
    "titulo":      "O Programador Pragmático",
    "autor":        "Andrew Hunt",
    "ano":      1999,
    "disponivel":       True,
}

# Acesse os  pelas chaves
print("Títulos :", livro["titulo"])
print("Autor   :", livro["autor"])
print("Ano     :", livro["ano"])
print("Status  :", "Disponível" if livro["disponivel"] else "Emprestado")


# MODIFICANDO E CONSULTANDO

# Atualizando um valor existente
livro["disponivel"] = False
print("\nApós emprestimo:", livro["disponivel"])

# Adicionando uma nova chave
livro["paginas"] = 352
print("Páginas:", livro["paginas"])

editora = livro.get("editora", "Não informada\n")
print( "Editora:", editora)


# CATÁLOGO: LISTA DE DICIONARIO

catalogo =[
    {"titulo": "O Programador Pragmático", "autor": "Andrew Hunt", "ano": 1999, "disponivel": True},
    {"titulo": "Código Limpo", "autor": "Robert C. Martin", "ano": 2008, "disponivel": False},
    {"titulo": "Entendo Algoritimo", "autor": "Aditya Bhargava", "ano": 2016, "disponivel": True},
    {"titulo": "A Hipótese do Amor", "autor": " Ali Hazelwood", "ano": 2022, "disponivel": True},
]

print("=== Catálogo da biblioteca ===\n")

#Percorrendo cada livro

for i, livro in enumerate(catalogo, start=1):
    status = "Disponivel" if livro ["disponivel"] else "Emprestado"
    print(f"{i}  {livro['titulo']} ({livro["ano"]})")
    print(f"  Autor:  {livro['autor']} | {status}")
    print("  "+ "-" *40)


# ---CONSULTAS E FILTROS---
print ("\n=== Livros disponiveis ===")
for livro in catalogo:
    if livro["disponivel"]:
       print(f"  {livro["titulo"]}")

print("\n=== Busca por Títulos ===")
busca = input("Digite o Título (ou parte): ").lower()
encontrado = False
for livro in catalogo:
    if busca in livro["titulo"].lower():
        print(f'Encontrado: {livro["titulo"]} - {livro["autor"]}')
        encontrado = True
if not encontrado:
    print ("Nenhum livro encontrado com esse termo.")

print("\n === Atributos do primeiro livro ===")
for chave, valor in catalogo[0].items(): 
    print (f" {chave}: {valor}")
    print("\n=== Resumo do Catálogo ===")

Dis = 0
Emp = 0

for livro in catalogo:
    if livro["disponivel"]:
        Dis += 1
    else:
        Emp += 1

print(f"\nDisponíveis: {Dis} | Emprestados: {Emp}")