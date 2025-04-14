import os
os.system("cls || clear")

lista_numeros = []
QUANTIDADE_NUMEROS = 5

print("= solicitando números =")
for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"digite o {i+1}ª número: "))
    lista_numeros.append(numero)

maior = max(lista_numeros)
menor = min(lista_numeros)

print("\nmostrando números")

for i, numero in enumerate(lista_numeros, start=1):
    print(f"(i)ª número: {numero}")

print(f"\maior número: {maior}")
print(f"\menor número: {menor}")