def Entrada():
    try:
        valor1 = int(input("Digite o valor 1: "))
        valor2 = int(input("Digite o valor 2: "))
    except ValueError:
        print("Erro: você deve digitar apenas números inteiros.")
        return

    op = input("Digite a operação [* / + -]: ")
    if op not in ["+", "-", "*", "/"]:
        print("Operação inválida!")
        return

    msg = f"{valor1} {op} {valor2}"

    if op == "+":
        res = Soma(valor1, valor2)
    elif op == "-":
        res = Subtracao(valor1, valor2)
    elif op == "*":
        res = Multiplicacao(valor1, valor2)
    elif op == "/":
        res = Divisao(valor1, valor2)

    Saida(msg, res)


def Soma(valor1, valor2):
    return (valor1 + valor2)


def Subtracao(valor1, valor2):
    return (valor1 - valor2)


def Multiplicacao(valor1, valor2):
    return (valor1 * valor2)


def Divisao(valor1, valor2):
    return (valor1 / valor2)


def Saida(msg, resultado):
    print(f"Soma de {msg} = {resultado}")


Entrada()