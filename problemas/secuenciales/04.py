
# En países de habla inglesa, es común dar la estatura de una persona como la suma de una cantidad  de pies, más una cantidad de pulgadas, por ejemplo 3’ 2”. Desarrolle el programa que determine la estatura en metros dada su estatura en el formato inglés.

import os
os.system ("cls")

Pies = float(input("Ingrese la cantidad de pies: "))
Pulgadas = float(input("Ingrese la cantidad de pulgadas: "))

pies_metros = 0.3048 
pulgadas_metros = 0.0254

estatura_metros = Pies * pies_metros + Pulgadas * pulgadas_metros

print(f"La estatura en metros es: {estatura_metros} m")

    