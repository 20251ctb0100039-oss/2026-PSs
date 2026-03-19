# ==============================================================================
# Nome: [SEU NOME AQUI]
# Disciplina: Programação Estruturada | Aula 10
# Descrição: Sistema de Biblioteca com Persistência em TXT e Tratamento de Erros
# ==============================================================================

import os

# --- PERSISTÊNCIA DE DADOS (Arquivos) ---

def carregar_catalogo():
    """Lê os dados do arquivo .txt e transforma em lista de dicionários."""
    lista = []
    if os.path.exists("biblioteca.txt"):
        try:
            with open("biblioteca.txt", "r", encoding="utf-8") as f:
                for linha in f:
                    dados = linha.strip().split("|")
                    if len(dados) == 3:
                        lista.append({
                            "titulo": dados[0],
                            "autor": dados[1],
                            "disponivel": dados[2] == "True"
                        })
        except Exception as e:
            print(f"⚠️ Erro ao carregar arquivo: {e}")
    return lista

def salvar_catalogo(lista):
    """Grava a lista de dicionários no arquivo .txt separando por |."""
    try:
        with open("biblioteca.txt", "w", encoding="utf-8") as f:
            for livro in lista:
                f.write(f"{livro['titulo']}|{livro['autor']}|{livro['disponivel']}\n")
    except Exception as e:
        print(f"❌ Erro ao salvar dados: {e}")

# --- FUNÇÕES DO SISTEMA (Baseadas nas suas imagens) ---

def listar_livros(catalogo):
    print("\n" + "=" * 50)
    print("           CATÁLOGO DA BIBLIOTECA")
    print("=" * 50)
    if not catalogo:
        print(" [!] Nenhum livro cadastrado.")
    else:
        for i, livro in enumerate(catalogo, 1):
            status = "✅ Disponível" if livro["disponivel"] else "❌ Emprestado"
            print(f" {i}. {livro['titulo']} - {livro['autor']} [{status}]")
    print("=" * 50)

def adicionar_livro(catalogo):
    print("\n--- Adicionar Novo Livro ---")
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    
    if not titulo or not autor:
        print("❌ Erro: Título e Autor são obrigatórios.")
        return
    
    catalogo.append({"titulo": titulo, "autor": autor, "disponivel": True})
    salvar_catalogo(catalogo)
    print("✅ Livro cadastrado com sucesso!")

def buscar_livro(catalogo):
    print("\n--- Buscar Livro ---")
    termo = input("Digite parte do título: ").strip().lower()
    try:
        resultados = [l for l in catalogo if termo in l["titulo"].lower()]
        if not resultados:
            print(" Nenhum livro encontrado.")
            return
        
        print(f"\n {len(resultados)} resultado(s) encontrado(s):")
        for livro in resultados:
            status = "Disponível" if livro["disponivel"] else "Emprestado"
            print(f" • {livro['titulo']} - {livro['autor']} [{status}]")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")

def registrar_emprestimo(catalogo):
    listar_livros(catalogo)
    if not catalogo: return
    try:
        numero = int(input("\nNúmero do livro para EMPRÉSTIMO: "))
        livro = catalogo[numero - 1]
        
        if not livro["disponivel"]:
            print(f"⚠️ '{livro['titulo']}' já está emprestado.")
        else:
            livro["disponivel"] = False
            salvar_catalogo(catalogo)
            print(f"✅ Empréstimo registrado: '{livro['titulo']}'")
    except (ValueError, IndexError):
        print("❌ Entrada inválida! Digite um número da lista.")

def devolver_livro(catalogo):
    listar_livros(catalogo)
    if not catalogo: return
    try:
        numero = int(input("\nNúmero do livro para DEVOLUÇÃO: "))
        livro = catalogo[numero - 1]
        
        if livro["disponivel"]:
            print(f"⚠️ '{livro['titulo']}' já está na biblioteca.")
        else:
            livro["disponivel"] = True
            salvar_catalogo(catalogo)
            print(f"✅ Devolução registrada: '{livro['titulo']}'")
    except (ValueError, IndexError):
        print("❌ Entrada inválida! Digite um número da lista.")

# --- MENU PRINCIPAL (Tratamento Profissional) ---

def main():
    catalogo = carregar_catalogo()
    
    opcoes = {
        "1": ("Listar livros", listar_livros),
        "2": ("Adicionar livro", adicionar_livro),
        "3": ("Buscar livro", buscar_livro),
        "4": ("Registrar empréstimo", registrar_emprestimo),
        "5": ("Devolver livro", devolver_livro),
        "0": ("Sair", None)
    }

    while True:
        print("\n📚 SISTEMA DE BIBLIOTECA - v2")
        for chave, (descricao, _) in opcoes.items():
            print(f" [{chave}] {descricao}")
        
        try:
            escolha = input("\nSua escolha: ").strip()
            
            if escolha not in opcoes:
                raise ValueError(f"Opção '{escolha}' inválida.")
            
            if escolha == "0":
                print("\nEncerrando sistema... Até logo! 👋")
                break
            
            # Executa a função correspondente
            _, funcao = opcoes[escolha]
            funcao(catalogo)
            
        except ValueError as e:
            print(f"⚠️ {e}")
            continue
        except Exception as e:
            print(f"❌ Erro crítico: {e}")

if __name__ == "__main__":
    main()