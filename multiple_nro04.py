import os

arista=0.0

#input
arista=float(os.sys.argv[1])

#processing
area_cubo=6*(arista**2)
volumen_cubo=arista**3

#outpout
print("#######################################")
print("#hallar el area y volumen de un cubo")
print("#######################################")
print("#")
print("#######################################")
print("#arista                       :", arista)
print("#area                         :", area_cubo)
print("#volumen                      :", volumen_cubo)
print("#######################################")

#condicional multiple
#si el area es menor que el volumen, mostrar cubo grande
#si el area y volumen es igual , mostar cubo mediano
#si el area es mayor que el volumen, mostrar cubo pequeño
if (area_cubo<volumen_cubo):
    print("cubo grande")
if (area_cubo==volumen_cubo):
    print("cubo mediano")
if (area_cubo>volumen_cubo):
    print("cubo pequeño")
