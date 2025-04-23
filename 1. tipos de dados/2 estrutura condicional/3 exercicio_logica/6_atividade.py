import os
os.system("clear")

# Faça um algoritmo que mostre um menu com opções de um cardápio de restaurante
# para uma pessoa.
# A pessoa vai escolher o prato desejado digitando o código do prato.
# após escolher o prato, o algoritmo dev mostrar o nome e valor do prato escolhido.

# Entrada
opção: - int(input("""
codigo\t prato \t\t valor
1 \t picanha   \t\t R$ 25,00
2 \t Lasanha   \t\t R$ 25,00
3 \t strogonoff \t\t R$ 18,00
4 \t bife acebo  \t\t R$ 15,00
5 \t pão com ovo  \t\t R$5,00
                   
Digite a opção desejada:
                    """))

# processamento
match opção:
 case 1 :       
  prato = "picanha"
  valor = 20,00
 case 2 :
  prato ="lasanha"
  valor = 25,00
 case 3 :
  prato = "strogonoff"
  valor = 18,00
 case 4 :
  prato = "bife"
  valor = 15,00
 case 5 :
  prato ="pão com ovo"
  valor = 5,00

# saida
print(f"\nprato escolhido:{prato}")
print(f"\nvalor:{valor}")