import os
os.system("cls||clear")

lista_numeros = []
quantidade_numero = 0

for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    if numero < 0:
          numero = 0
   lista_numeros.append(numero)

print("\nlistando números")
for numero in lista_numeros:
     print(+"número: {numero}")