import os
os.system ("clear")

# Entrada
valor_produto = float(input("Digite o valor do produto: "))
forma_de_pagamento = int(input(""" 
1 - A vista
2 - A prazo
Digite a forma de pagamento: """))

 match forma_de_pagamento:
    case 1:
        # aplicando desconto de 10%
        desconto = valor_produto * 0.10
        valor_pagar = valor_produto - desconto

        # exibindo resultado.
      print(f"\nvalordo pagamento: R$ {valor_produto}")
                  print(f"forma de pagamento: à vista")
                  print(f"total da pagar: R${valor_pagar}")
    case 2:
        quantidade_parcelas = int(input("digite a quantidade deparcelas:"))
        if quantidade_parcelas >= 1 and quantidade_parcelas <= 6:
           valor_parcela = valor_produto / quantidade_parcelas

         # exibindo resultado.
                  print(f"\nvalor do produto: R${valor_produto}")
                  print(f"forma de pagamento: à prazo")
                  print(f"quantidade de parcela: {quantidade_de_parcelas}")
                  print(f"valor por parcela: R$ {valor_parcela:.2f}")
                  print(f"total à prazo: R${ valor_produto}") 
 else:
print("O parcelamento deve ser em até 6 parcelas.")   

         
