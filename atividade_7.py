import os

os.system("cls")

def logo():
    print("========")
    print(" SENAI ")
    print("========")

def somar(lista_numeros):
    soma = lista_numeros[0] + lista_numeros[1]
    return soma

def subtrair(lista_numeros):
    subtrair = lista_numeros[0] - lista_numeros[1]
    return subtrair

def multiplicar(lista_numeros):
    multiplicacao = lista_numeros[0] * lista_numeros[1]
    print(f"multplicação: {multiplicacao}")

def dividir(lista_numeros):
    divisao = lista_numeros[0] / lista_numeros[1]
    print(f"Divisão: {divisao}")

logo()
print("= Solicitando dados =")

lista_numeros= []
QUANTIDADE_NUMEROS = 2

for i in range(QUANTIDADE_NUMEROS):
    numero = int(input("Digite o {i+1}ª numero: "))
    lista_numeros.append(numero)

soma = somar(lista_numeros)
subtração = subtrair(lista_numeros)

logo()
print("= Exibindo dados =")
print(f"Soma: {soma}")
print(f"Subtrair: {subtração}")
multiplicar(lista_numeros)
dividir(lista_numeros)
