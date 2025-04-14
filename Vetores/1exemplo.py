import os
os.system("cls || clear")

# criando uma lista.
lista_notas = []

# Adicionando 3 notas em uma lista>
for i in range(3):
    nota = float(input("digite uma nota:"))
    lista_notas.append(nota)

# soma
soma = sum(lista_notas)

# exibindo todos os valores em uma lista.
print()
for nota in lista_notas: # foreach
    print(nota)