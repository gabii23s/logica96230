import os
from datetime import date
os.system("cls || clear")

def calcular(idade):
    resultado = date.today().year - idade
    return resultado

ano_nascimento = int(input("digite o ano de nascimento: "))

idade = calcular(ano_nascimento)

print(f"idade: {idade}")