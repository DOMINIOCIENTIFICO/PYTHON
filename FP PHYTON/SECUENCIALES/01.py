
import os
os.system("cls") 
#Desarrolle el programa que determine el porcentaje de varones y de mujeres que hay en un salón de clases.

varones = int (input("Varones :  "))
mujeres = int (input("Mujeres :  "))
total = varones + mujeres
pVarones = varones  * 100.0 / total
pMujeres = mujeres  * 100.0 / total



print(f"% Varones :{pVarones:.2f} %")
print(f"% mujeres :{pMujeres:.2f} %")
print(pMujeres)






