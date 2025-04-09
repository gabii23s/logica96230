import os

os.system("cls || clear")

def calcular_media(nota1, nota2):
    soma = nota1 + nota2 
    resultado = soma / 2
    return resultado

def verificar_resultado(media):
    if media >= 7:
        print("Aprovado.")
    else:
        print("Reprovado.")

nota1 = float(input("digite a primeira nota:"))
nota2 = float(input("digite a segunda nota:"))
media = calcular_media(nota1, nota2,)
print({media})
verificar_resultado(media)