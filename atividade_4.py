import os

os.system("cls")

def logo():
    print("========")
    print(" SENAI ")
    print("========")

# Funçao COM parametro e COM retorno
def somar(a, b):
    return a + b


# Funçao COM paramentro e COM retorno
def subtrair(a, b):
    return a - b


# Funçao parametro e SEM retorno
def multiplicar(a, b):
    multiplicacao = a * b
    print(f"multplicação: {multiplicacao}")


# Função COM parametro e SEM retorno.
def dividir(a, b):
    divisao = a / b
    print(f"Divisão: {divisao}")

logo()
print("= Solicitando dados =")
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

soma = somar(n1, n2)
subtração = subtrair(n1, n2)

logo()
print("= Exibindo dados =")
print(f"Soma: {soma}")
print(f"Soma: {subtração}")
multiplicar(n1, n2)
dividir(n1, n2)
