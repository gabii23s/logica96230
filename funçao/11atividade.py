import os
os.system("cls || clear")

def inflacionar(preco):
    if preco < 100:
        resultado = preco *1.10 # inflaciona 10%
    else:
        resultado = preco * 1.20 # inflacona 20%
    return resultado

def descontar(preco):
    if preco < 100:
        resultado = preco * 0.10 # descontar10%
    else:
        resultado = preco * 0.20 # descontar 20%
    return resultado


preco_produto = float(input("digite o peço do produto:"))

preco_inflacionado = inflacionar(preco_produto)
preco_descontar = descontar(preco_produto)

print(f"preço com aumento: {preco_inflacionado}")
print(f"valor do desconto: {preco_descontar} ")

