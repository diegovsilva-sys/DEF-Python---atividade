import os

#   Limpa o terminal.
# Cabeçalho.
# Função.
# Sem retorno.
#Sem parâmetro.
def logo_senai():
    os.system("cls")
    print("===== =====")
    print("SENAI")
    print("===== =====")

# Chamar a função.
logo_senai()
nome = input("Digite seu nome: ")

logo_senai()
idade = int(input("Digite sua idade: "))

logo_senai()
peso = float(input("Digite seu peso: "))


