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

class Pet:
    def __init__(self, nome, especie, idade, raca, peso, nome_dono, vacinado):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.hospedado = False
        
        self.raca = raca
        self.peso = peso
        self.nome_dono = nome_dono
        self.vacinado = vacinado

    def exibir_dados(self):
        print(f"\n--- Ficha Técnica: {self.nome} ---")
        print(f"Espécie: {self.especie} | Raça: {self.raca}")
        print(f"Dono(a): {self.nome_dono}")
        print(f"Peso atual: {self.peso}kg")

    def registrar_entrada(self):
        if self.hospedado:
            print(f"Aviso: {self.nome} já está hospedado.")
            return

        if not self.vacinado:
            print(f"Entrada negada: {self.nome} não está vacinado.")
            return

        self.hospedado = True
        print(f"Check-in realizado: {self.nome} entrou no hotel.")

    def registrar_saida(self):
        if self.hospedado:
            self.hospedado = False
            print(f"Check-out realizado: {self.nome} saiu do hotel.")
        else:
            print(f"Aviso: {self.nome} não está hospedado no momento.")

    def calcular_diaria(self):
        if self.idade <= 3:
            return 50.00
        elif self.idade <= 10:
            return 60.00
        else:
            return 75.00

    def verificar_vacinacao(self):
        if self.vacinado:
            print(f"Status: Vacinação de {self.nome} está em dia.")
        else:
            print(f"Alerta: {self.nome} precisa atualizar as vacinas!")

    def atualizar_peso(self, novo_peso):
        self.peso = novo_peso
        print(f"O peso de {self.nome} foi atualizado para {self.peso}kg.")

    def emitir_resumo(self):
        status_hosp = "Hospedado" if self.hospedado else "Não hospedado"
        diaria = self.calcular_diaria()
        
        print(f"\n" + "="*30)
        print(f"RESUMO COMPLETO - HOTEL PET")
        print(f"="*30)
        print(f"Pet: {self.nome} ({self.raca})")
        print(f"Idade: {self.idade} anos")
        print(f"Responsável: {self.nome_dono}")
        print(f"Status Atual: {status_hosp}")
        print(f"Valor da Diária: R$ {diaria:.2f}")
        print(f"="*30 + "\n")

    def pode_ser_hospedado(self):
        if not self.vacinado:
            print(f"{self.nome} não pode ser hospedado (vacinação pendente).")
            return False
        return True
    def aplicar_desconto(self, porcentagem):
        diaria = self.calcular_diaria()
        desconto = diaria * (porcentagem / 100)
        nova_diaria = diaria - desconto

        print(f"Desconto aplicado: {porcentagem}%")
        print(f"Valor com desconto: R$ {nova_diaria:.2f}")
        return nova_diaria



pet1 = Pet("Rex", "Cachorro", 5, "Labrador", 22.5, "Maria", True)
pet2 = Pet("Mimi", "Gato", 2, "Siamês", 4.2, "João", True)
pet3 = Pet("Thor", "Cachorro", 11, "Vira-lata", 18.0, "Ana", False)

pet1.exibir_dados()
pet1.registrar_entrada()
pet1.verificar_vacinacao()
pet1.emitir_resumo()

pet2.exibir_dados()
pet2.registrar_entrada()
pet2.verificar_vacinacao()
pet2.emitir_resumo()

pet3.exibir_dados()
pet3.verificar_vacinacao()
pet3.atualizar_peso(19.5)
pet3.emitir_resumo()

print("\n--- TESTE DESCONTO ---")
pet1.aplicar_desconto(10)

print("\n--- TESTE SAÍDA ---")
pet1.registrar_saida()
pet1.registrar_saida()


pets = [pet1, pet2, pet3]

print("\n--- RESUMO GERAL DOS PETS ---")

for pet in pets:
    pet.emitir_resumo()

