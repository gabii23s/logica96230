import os

os.system("cls || clear")

login_ = "Gabriella"
senha_ = 237045

while True:
 login = input("digite sua login:")
 senha = input("digite sua senha:")

 if login_ == login and senha_ == senha:
  print("usuario e senha corretos!") 
  print("usuario e senha corretos!") 
  break

 else:
        print("senha ou login inválidos")
       
print(f"login {login}")
print(f"senha {senha}")

print("fim")