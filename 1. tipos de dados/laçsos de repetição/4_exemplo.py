import os

os.system ("cls || clear")

while True:
    idade = int(input("digite sua idade: "))

    if idade < 18:
        print("somente maior que de  18 anos.\n")

    else:
        print("senha ou login inválidos")
        break
    
    print("fim")