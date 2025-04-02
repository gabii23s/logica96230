import os

# função sem retorno
def logo_senai():
    os.system("cls || clear")
    print("== senai ==")

logo_senai() # chamando a função
nome = input("digite seu nome: ")

logo_senai( ) # chamando a função
idade = int(input("digite sua idade: "))

logo_senai() # chamando a função
print(f"nome: {nome}")
print(f"idade: {idade}")