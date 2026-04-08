import os

os.system("cls")

def logo():
    print("========")
    print(" SENAI ")
    print("========")

def somar(a, b):
    return a + b

print("= Solicitando dados =")
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

soma = somar(n1, n2)

logo()
print("= Exibindo dados =")
print(f"Soma: {soma}")
