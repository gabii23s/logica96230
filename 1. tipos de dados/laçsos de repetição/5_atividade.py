import os 
os.system ("cls || clear")

soma = 0
quantidade = 0

while True:
    numero = int(input("digite um número:"))

    if numero < 0:
        break

    soma += numero
    quantidade += 1
    
if quantidade > 0:
    media = soma / quantidade
    print (f"A media que você deseja : {media:.2}")
else:
    print("número negado")
