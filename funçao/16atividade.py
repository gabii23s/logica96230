import os
os.system("cls || clear")

peso = float(input("digite seu peso: "))
altura = (float(input("digite a sua altura:")))

def calcular_imc(peso, altura):     
    imc = peso / altura **2
    return imc

if calcular_imc (peso , altura) < 18.5:
    print("Abaixo do peso.")
elif calcular_imc (peso, altura) < 24.9:
    print("peso normal")
elif calcular_imc (peso, altura) <29.9:
    print("sobrepeso")
elif calcular_imc (peso, altura) <34.9:
    print("obesidade grau 1")
elif calcular_imc (peso, altura) < 39.9:
    print("obesidade grau 2")
else:
    print("obesidae grau 3") 

print(f"o seu imc é: {calcular_imc(peso,altura)}")