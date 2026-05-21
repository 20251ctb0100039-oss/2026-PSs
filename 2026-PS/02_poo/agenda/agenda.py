'''
======================================================================
# ARQUIVO      : pet.py
# Disciplina   : Programação de Sistemas (2026-2)
# Aula         : Aula 20 - Por que POO?
# Autor        : Gabriele Bueno Martins
# Conceitos    : Classes, objeto, atributos, métodos, encapsulamento    
# Atividade    : Classe Pet
======================================================================
'''

import os
import pickle

class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def exibir(self):
        print(f" Nome     : {self.nome}")
        print(f" Telefone : {self.telefone}")
        print(f" Email    : {self.email}")

def cadastrar(contatos):
    print("\n--- Novo contato ---")
    nome = input("Nome     : ")
    telefone = input("Telefone : ")
    email = input("Email    : ")
    contatos.append(Contato(nome, telefone, email))
    print("√ Contato cadastrado.")

def listar(contatos):
    if not contatos:
        print("\n(agenda vazia)")
        return
    print(f"\n--- Agenda ({len(contatos)} contatos) ---")
    for i, c in enumerate(contatos, start=1):
        print(f"\n[{i}]")
        c.exibir()

def remover(contatos):
    listar(contatos)
    if not contatos:
        return
    try:
        indice = int(input("\nNº do contato a remover: ")) - 1
        if 0 <= indice < len(contatos):
            removido = contatos.pop(indice)
            print(f"√ Contato '{removido.nome}' removido.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida. Digite um número.")

def salvar_em_binario(contatos, caminho):
    with open(caminho, "wb") as arquivo:
        pickle.dump(contatos, arquivo)
    print(f"√ {len(contatos)} contato(s) salvo(s) em {caminho}")

def carregar_de_binario(caminho):
    try:
        with open(caminho, "rb") as arquivo:
            return pickle.load(arquivo)
    except FileNotFoundError:
        print(f"Arquivo {caminho} ainda não existe. Começando vazio.")
        return []

def menu():
    caminho_bin = "agenda.bin"
    contatos = carregar_de_binario(caminho_bin)
    
    while True:
        print("\n========== AGENDA ==========")
        print("1 - Cadastrar contato")
        print("2 - Listar contatos")
        print("3 - Remover contato")
        print("0 - Sair")
        opcao = input("Opção: ")

        if opcao == "1":
            cadastrar(contatos)
        elif opcao == "2":
            listar(contatos)
        elif opcao == "3":
            remover(contatos)
        elif opcao == "0":
            salvar_em_binario(contatos, caminho_bin)
            print("Até logo!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()