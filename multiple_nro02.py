import os

pi,semieje_menor,semieje_mayor=0.0,0.0,0.0

#input
pi=float(os.sys.argv[1])
semieje_menor=float(os.sys.argv[2])
semieje_mayor=float(os.sys.argv[3])

#processing
area_elipse=pi*semieje_mayor*semieje_menor

#outpout
print("##################################")
print("#calcular el area de un elipse")
print("##################################")
print("#")
print("##################################")
print("#vaor del pi             :", pi)
print("#semieje menor           :", semieje_menor)
print("#semieje mayor           :", semieje_mayor)
print("#area                    :", area_elipse)
print("##################################")

#condicional multiple
#si el semieje mayor es mayor que el menor , la elipse es horizontal
#si el semieje mayor es menor que el menor , la elipse es vertical
#si el semieje mayor es igual que el menor , la elipse es un circulo
if (semieje_menor<semieje_mayor):
    print("elipse horizontal")
if (semieje_mayor<semieje_menor):
    print("elipse vertical")
if (semieje_menor==semieje_mayor):
    print("circulo")
