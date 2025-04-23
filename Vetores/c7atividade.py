import os
os.system("cls||clear")

vetor = []
quant_negativos = 0
soma_positivos = 0

def solicitar_dados():
    vetor = []
    for i in range(5):
        numero = float(input(f"Digite o {i+1}º número: "))
        vetor.append(numero)
    return vetor

def verificar_positivo_negativo(lista):
    quant_negativos = 0
    soma_positivos = 0
    for numero in lista:
        if numero < 0:
            quant_negativos += 1
        else:
            soma_positivos += numero
    return quant_negativos, soma_positivos

lista = solicitar_dados()
quant_negativos,soma_positivos = verificar_positivo_negativo(lista)
print("Quantidade de números negativos:", quant_negativos)
print("Soma dos números positivos:", soma_positivos)
