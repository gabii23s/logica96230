import os
os.system ("cls||clear")

while True:
    nota = float(input("digite uma nota: "))

if nota < 0 or nota > 10:
    print("A nota deve ser entre 0 e 10.\n")
else:
    break

print(f"nota {nota}")
