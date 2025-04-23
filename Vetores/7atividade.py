import os
os.system("cls||clear")

vetor = []
quant_negativos = 0
soma_positivos = 0

for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    vetor.append(numero)

    if numero < 0:
        quant_negativos += 1
    else:
        soma_positivos += numero

print("\nVetor preenchido:", vetor)
print("Quantidade de números negativos:", quant_negativos)
print("Soma dos números positivos:", soma_positivos)