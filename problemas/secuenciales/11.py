# Dados dos números enteros de 3 cifras, desarrolle el programa que muestre:
# la primera y tercera cifras intercambiadas entre ambos.
# Ejemplo: 123 y 456 → 624 y 351

import os
os.system("cls")

# Solicitar los dos números de 3 cifras
num1 = int(input("Introduce el primer número de 3 cifras: "))
num2 = int(input("Introduce el segundo número de 3 cifras: "))

# Extraer las cifras de ambos números
# Para el primer número
c1_1 = num1 // 100  # Primera cifra
c2_1 = (num1 // 10) % 10  # Segunda cifra
c3_1 = num1 % 10  # Tercera cifra

# Para el segundo número
c1_2 = num2 // 100  # Primera cifra
c2_2 = (num2 // 10) % 10  # Segunda cifra
c3_2 = num2 % 10  # Tercera cifra

# Intercambiar la primera y tercera cifra de ambos números
nuevo_num1 = c3_2 * 100 + c2_1 * 10 + c1_1
nuevo_num2 = c3_1 * 100 + c2_2 * 10 + c1_2

# Mostrar el resultado
print(f"Nuevo número 1: {nuevo_num1}")
print(f"Nuevo número 2: {nuevo_num2}")