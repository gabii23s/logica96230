import os

os.system("cls || clear")

login_ = "Gabriella"
senha_ = 237045

for i in range(3):
   login = input("digite sua login:")
   senha = input("digite sua senha:")

   if login_ == login and senha_ == senha:
     print("acesso permitido!")
   break

else:
  print("Acesso negado. \n")
if i == 2:
       print("Número de tentativa acima do permitido")

print("fim")