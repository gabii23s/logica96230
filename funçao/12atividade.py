import os
os.system("cls || clear")

def descontar(preco):
    if preco < 100:
        resultado = preco * 0.10 # descontar10%
    else:
        resultado = preco * 0.20 # descontar 20%
    return resultado

preco_produto = float(input("digite o peço do produto:"))

preco_descontar = descontar(preco_produto)

print(f"preço final: {preco_descontar}")



