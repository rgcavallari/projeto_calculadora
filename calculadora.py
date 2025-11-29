import math

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

def potencia(a, b):
    return a ** b

def raiz(a):
    if a < 0:
        return "Erro: raiz de número negativo!"
    return math.sqrt(a)

def media(lista):
    return sum(lista) / len(lista)

def menu():
    print("\n===== CALCULADORA INTERMEDIÁRIA =====")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Potência")
    print("6 - Raiz Quadrada")
    print("7 - Média")
    print("0 - Sair")

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    try:
        if opcao == "1":
            a = float(input("Número 1: "))
            b = float(input("Número 2: "))
            print("Resultado:", soma(a, b))

        elif opcao == "2":
            a = float(input("Número 1: "))
            b = float(input("Número 2: "))
            print("Resultado:", subtracao(a, b))

        elif opcao == "3":
            a = float(input("Número 1: "))
            b = float(input("Número 2: "))
            print("Resultado:", multiplicacao(a, b))

        elif opcao == "4":
            a = float(input("Número 1: "))
            b = float(input("Número 2: "))
            print("Resultado:", divisao(a, b))

        elif opcao == "5":
            a = float(input("Base: "))
            b = float(input("Expoente: "))
            print("Resultado:", potencia(a, b))

        elif opcao == "6":
            a = float(input("Número: "))
            print("Resultado:", raiz(a))

        elif opcao == "7":
            qnt = int(input("Quantos números vai inserir? "))
            valores = []
            for i in range(qnt):
                valores.append(float(input(f"Valor {i+1}: ")))
            print("Média:", media(valores))

        elif opcao == "0":
            print("Encerrando...")
            break

        else:
            print("Opção inválida!")

    except ValueError:
        print("Erro: digite apenas números!")

