import os

os.system("cls")

#Função com parametros.
def calcular_media(n1, n2):
    media = (n1 + n2) / 2
    return media

#Exemplo de uso da função.
def verificar_resultados(media):
    if media >= 7:
        resultado = "Aprovado"
    else:
        resultado = "Reprovado"
    return

print("= Solicitando dados =")
n1 = int(input("Digite o primeira nota: "))
n2 = int(input("Digite o segunda nota: "))

media = calcular_media(n1, n2)
resultado = verificar_resultados(media)
