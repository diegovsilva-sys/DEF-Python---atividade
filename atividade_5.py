import os
os.system("cls")

def logo():
    print("========")
    print(" SENAI ")
    print("========")

#Funcao COM parametro e COM retorno
def medir(a, b):
    return a * 100
    
logo()
print("= Solicitando dados =")
metros = int(input("Digite um numero: "))

medição = medir(metros, 100)

logo()
print("= Exibindo dados =")
print(f"Centimetros: {medição}cm")