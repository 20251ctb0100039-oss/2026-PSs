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

import sys
import os
import pickle

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pet import Pet

ARQUIVO_BIN = "pets.bin"
ARQUIVO_TXT = "pets.txt"

def salvar_dados(lista_pets):
    with open(ARQUIVO_BIN, "wb") as f:
        pickle.dump(lista_pets, f)
    
    with open(ARQUIVO_TXT, "w", encoding="utf-8") as f:
        f.write("--- RELATÓRIO DO HOTEL PETVILLE ---\n")
        for p in lista_pets:
            status = "Hospedado" if p.hospedado else "Não Hospedado"
            f.write(f"Nome: {p.nome} | Espécie: {p.especie} | Status: {status}\n")
    print("\n Dados salvos!")

def carregar_dados():
    if os.path.exists(ARQUIVO_BIN):
        try:
            with open(ARQUIVO_BIN, "rb") as f:
                return pickle.load(f)
        except:
            return []
    return []

def menu():
    print("\n" + "="*35)
    print(" HOTEL PETVILLE - SISTEMA V2.0")
    print("="*35)
    print("1. Cadastrar novo Pet")
    print("2. Listar todos (Ficha)")
    print("3. Check-in / Check-out")
    print("4. Atualizar peso")
    print("5. Buscar por nome")
    print("6. Relatório Financeiro")
    print("7. Resumo Individual")
    print("0. Salvar e Sair")
    return input("\nEscolha uma opção: ")

pets = carregar_dados()

while True:
    op = menu()

    if op == "1":
        nome = input("Nome: ")
        esp = input("Espécie: ")
        idade = int(input("Idade: "))
        raca = input("Raça: ")
        peso = float(input("Peso: "))
        dono = input("Dono: ")
        vacina = input("Está vacinado? (s/n): ").lower() == 's'
        
        novo = Pet(nome, esp, idade, raca, peso, dono, vacina)
        pets.append(novo)
        print(f"{nome} cadastrado!")

    elif op == "2":
        if not pets:
            print("Nenhum pet cadastrado.")
        for p in pets:
            p.exibir_dados()

    elif op == "3":
        busca = input("Nome para Check-in/out: ").lower()
        for p in pets:
            if p.nome.lower() == busca:
                sub = input("1. Entrada | 2. Saída: ")
                if sub == "1": p.registrar_entrada()
                elif sub == "2": p.registrar_saida()
                break
        else: print("Pet não encontrado.")

    elif op == "4":
        busca = input("Nome do pet: ").lower()
        for p in pets:
            if p.nome.lower() == busca:
                novo_p = float(input(f"Novo peso para {p.nome}: "))
                p.atualizar_peso(novo_p)
                break

    elif op == "5":
        termo = input("Digite parte do nome: ").lower()
        for p in pets:
            if termo in p.nome.lower():
                print(f"-> {p.nome} ({p.especie})")

    elif op == "6":
        total = 0
        print("\n--- HOSPEDADOS ---")
        for p in pets:
            if p.hospedado:
                valor = p.calcular_diaria()
                total += valor
                print(f" {p.nome} | R$ {valor:.2f}")
        print(f"Total: R$ {total:.2f}")

    elif op == "7":
        busca = input("Nome para resumo: ").lower()
        for p in pets:
            if p.nome.lower() == busca:
                p.emitir_resumo()
                break

    elif op == "0":
        salvar_dados(pets)
        print("Saindo...")
        break

    else:
        print("Opção inválida!")