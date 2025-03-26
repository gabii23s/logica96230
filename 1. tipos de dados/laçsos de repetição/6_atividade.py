import os 
os.system ("cls || clear")

quantidade_pares = 0
quantidade_impares = 0
soma_pares = 0
soma_total = 0
total = 0

while True:
    numero = int(input("digite um numero inteiro:"))

    if numero == 0:
        break

    soma_total += numero
    total == 1

    if numero % 2 == 0:
        quantidade_pares += 1
        soma_pares += numero
    else:
        quantidade_impares += 1

total_pares = soma_pares / quantidade_pares if quantidade_pares > 0 else 0

media = soma_total / total if total > 0 else 0

print(f"quantidades pares: {quantidade_pares}")
print(f"quantidades impares: {quantidade_impares}")
print(f"Total dos números pares: {total_pares}")
print(f"total geral: {total}")