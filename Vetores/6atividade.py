import os
os.system("cls||clear")

lista_pratos = []

while True:

    opcao = int(input("""
Código \t Prato \t\t valor
1 \t Picanha \t\t R$ 25,00
2 \t Lasanhas\t\t R$ 20,00
3 \t Strogonnoff \t\t 18,00
4 \t Bife acebolado \t R$ 15,00
5 \t Pão com ovo \t\t R$ 5,00
                     
Digite a opção desejada: """))

    match opcao:
        case 1:
            prato = "picanha"
            preco =25
        case 2:
            prato = "Lasanha"
            preco = 20
        case 3:
            prato = "strogonnoff"
            preco = "18"
        case 4:
            prato = "Bife acebolado"
            preco = "15"
        case 5:
            prato = "Pão com ovo"
            preco = 5
        case _:
            print("Opção inválida. \ntente novamente.")
            prato =""
            prco = 0

    lista_pratos = append(prato)
    precos_pratos= append(preco)

    print("deseja escolher outro prato?")
