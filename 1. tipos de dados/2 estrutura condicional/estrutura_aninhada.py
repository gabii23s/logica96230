import os
os.system("clear")

idade = 16

# se idade <12 emtao
#     escreval ("acesso negado.")
# senao se idade < 18 entao
#     escreval("somente com permissão dos pais.")
# senao
#     escreval("acesso permitido.")
#fimse


if idade < 12:
  print("acesso negado.")
elif idade < 18:
   print("somente com permissão dos pais.")
else:
   print("acesso permitido.")


print("== fim ==")