import os

os.system("cls")

#Função com parametros.
def saudacao(nome):
    print(f"Ola, {nome}!")
    print("Bem vindo(a) ao nosso site!")

    #Exemplo de uso nda função.
    nome_visitante = input("Digite seu nome: ")
    saudacao("nome=nome_visitante")
