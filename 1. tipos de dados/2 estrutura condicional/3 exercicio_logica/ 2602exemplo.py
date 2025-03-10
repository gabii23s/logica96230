# impoar p terminal.
import os
os.system("clear")

# faça um algoritmo que solicite ao usuário dois números
# e um caractere que calcula as operações básicas (+-*/).
# mostre os números informados pelo usuário,
# o operador escolhido eo resultado.

# Entrada
primeiro_numero = int(input("digite um número: "))
operador = input("digite a operação que deseja(=-*/): ")
segundo_numero = int(input("digite um numero: ")) 

# processamento
match operador:
    case "+":
        resultado = primeiro_numero + segundo_numero
    case "-":
        resultado = primeiro_numero - segundo_numero
    case "*":
        resultado = primeiro_numero * segundo_numero
    case "/":
        resultado = primeiro_numero / segundo_numero
    case "_":
        resultado = "opção inválida."

# saida
print(f"\nprimeiro número: {primeiro_numero}")
print(f"operação:{operador}")
print(f"segundo número:{segundo_numero}")
print(f"resultado:{resultado}")