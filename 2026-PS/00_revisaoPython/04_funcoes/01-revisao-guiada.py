# =================================================================
# NOME: Gabriele Bueno Martins
# DISCIPLINA: Lógica de Programação 
# DATA: 09/03/2026
# DESCRIÇÃO: Sisema de Calculos de imc
# =================================================================



# FUNÇÃO PARAMETRO
def exibir_cabecalho():
    print("+"*40)
    print("\n      Sistema de Cálculo de IMC\n")
    print("+"*40)

# Chama a função
exibir_cabecalho()

# FUNÇÃO COM PARÂMETROS E RETORNO

def calcular_imc(peso, altura):
    imc = peso/ (altura **2)
    return imc
peso = float(input("Peso (kg): "))
altura =  float(input("Altura (m): "))

resultado = calcular_imc(peso, altura)
print (f"Seu IMC é : {resultado:.2f}\n\n")

# ESCOPO LOCAL vs. global

versao = "1.0" 

def demonstrar_escopo():
    mensagem = "Olá do interior da função"      
    print ("Dentro  da Função:")
    print (f" mensagem = {mensagem}")       
    print (f"versão = {versao}")        
demonstrar_escopo()
print ("\nFora da Função:")
print (f"versão = {versao}\n")        

#Tentativa versão
def mostrar_versao():
    print(f"Sistema IMC--versão {versao}")

mostrar_versao()

# VALOR PADRÃO E MÚLTIPLOS RETORNOS

def classificar_imc(imc, unidades="kg/m²"):
    # Classificar o IMC e retorna classificação e emoji de status.
    # Parametro 'unidade' tem valor padrão 

    if imc < 18.5:
        classificacao = "Abaixo do peso"
        emoji = "⬇"
    elif imc < 25.0:
        classificacao = "Peso normal"
        emoji = "✅"
    elif imc <30.0:
        classificacao = "Sobrepeso"
        emoji = "⚠"
    else:
        classificacao = "Obesidade"
        emoji = "🔴"
    return classificacao, emoji

classificacao, emoji = classificar_imc(resultado)
print(f"IMC {resultado:.2f} ({classificacao}) {emoji}")

# Recursção bASICA
def contagem_regressiva(n):
    if n <0:
        return
    print(n)
    contagem_regressiva(n-1)

print("\n=== Contagem regressiva ===")
contagem_regressiva(5)

# Fatorial : exemplo de recursão com retorno
def fatorial(n):
    if n ==0 or n==1:
        return 1
    return n *fatorial(n-1)

print("\n --- Fatorial ---")
for i in range (1, 7):
    print(f"{i}! = {fatorial (i)}")

# Função principal

def processar_pessoa():
    nome = input("\nNome: ")
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))

    imc = calcular_imc(peso, altura)

    classificacao, emoji = classificar_imc(imc)

    print("\n****** Resultado ******")
    print(f"Nome          : {nome}")
    print(f"IMC           : {imc:.2f} kg/m²")
    print(f"Classificação : {classificacao} {emoji}")

# Execução prinicpal

exibir_cabecalho()

continuar ="s"
while continuar =="s":
    processar_pessoa()
    continuar = input("\n Processar outra pessoa? (s/n): ").lower()

