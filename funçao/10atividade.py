import os
os.system("cls || claer")

def converter_centimetros(metros):
    return metros * 100;

print("= CONVERTER METROS PARA CENTÍMETROS =")
metros = float(input("digite um núnero: "))

centimetros = converter_centimetros(metros)

print("\n= RESULTADOS =")
print(f"{metros} metros é igual a {centimetros} centimetros.")