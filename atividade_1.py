import os
import time
os.system("cls")

#Função com parametros.
def tabuada(numero):
    numero = int(input("Digite um numero: "))

#Exemplo de uso da função.

os.system("cls")
numero = int(input("Digite um numero: "))

for i in range(1, 11):
    
    print(f"\nTabuada de {numero}: ")
    print("_" * 15)
    time.sleep(1.25)

# range(1, 11) vai de 1 até 10 (*o último numero é exclusivo)

    
    resultado = numero * i
    #f-string para formatar a saida d forma organizada
    print(f"{numero} x {i} = {numero * i}")
    print("-" * 15)
