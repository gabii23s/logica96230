import os
os.system("cls || clear")

lista_numeros = []
QUANTIDADE_NUMEROS = 6

def pares_impares(lista):
    pares = 0
    impares = 0
    for numero in lista:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

print("= solicitando números =")
for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"digite o {i+1}ª número: "))
    lista_numeros.append(numero)

pares, impares = pares_impares(lista_numeros)


print("\nmostrando números")

for i, numero in enumerate(lista_numeros, start=1):
    print(f"(i)ª número: {numero}")

print(f"\Quantidades pares: {pares}")
print(f"\Quantidades impares: {impares}")