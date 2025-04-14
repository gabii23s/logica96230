import os
os.system("cls || clear")

lista_notas = []
QUANTIDADE_NOTAS = 4
for i in range(QUANTIDADE_NOTAS):
    nota = float(input("digite uma nota:"))
    lista_notas.append(nota)

media= sum(lista_notas) / QUANTIDADE_NOTAS

print()
for nota in lista_notas:
    print(nota)
if media >= 7:
    print("você esta aprovado!")

elif media >=5:
    print("você esta na recuperação!")

else:
    print("reprovado!")
print(f"Média: {media}")