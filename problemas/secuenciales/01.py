#Desarrolle el programa que determine el porcentaje de varones y de mujeres que hay en un salón  de clases

import os
os.system("cls")

Varones=int(input("Varones: "))
Mujeres=int(input("Mujeres: "))

total = Varones + Mujeres
pVarones=Varones*100.0/total
pMujeres=Mujeres*100.0/total

print(f"% de varones: {pVarones:.2f}%")
print(f"% de mujeres: {pMujeres:.2f}%")















