import os

os.system("cls || clear")
def logo_senai():
    print("=== senai Dendezeiros ===")

def somar(n1, n2) :
    return n1 + n2

def subtrair(n1, n2) :
    return n1 - n2

logo_senai()
n1 = int(input("digite o primeiro número: "))

logo_senai()
n2 = int(input("digite o segundo número: "))

soma = somar(n1, n2)
subtracao = subtrair(n1, n2)
logo_senai()
print(f"soma: {soma}")
print(f"subtração: {subtracao}")