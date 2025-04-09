import os

os.system("cls || clear")

def calcular_media(nota1, nota2, nota3):
    soma = nota1 + nota2 + nota3
    resultado = soma / 3
    return resultado


nota1 = float(input("digite a primeira nota:"))
nota2 = float(input("digite a segunda nota:"))
nota3 = float(input("digite a terceira nota"))
media = calcular_media(nota1, nota2, nota3)
print({media})

