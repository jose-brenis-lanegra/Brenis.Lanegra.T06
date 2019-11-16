import os

pi,radio=0.0,0

#input
pi=float(os.sys.argv[1])
radio=int(os.sys.argv[2])

#processing
volumen_esfera=(4*pi*(radio**3))/3

#outpout
print("###################################")
print("#hallar el volumen de una esfera")
print("###################################")
print("#")
print("###################################")
print("#el valor de pi             :", pi)
print("#radio                      :", radio)
print("#volumen                    :", volumen_esfera)
print("###################################")

#condicional multiple
#si el volumen es menor que su radio, mostrar incoherente
#si el volumen es igual que el radio, mostrar coincidencia
#si el volumen es mayor que el radio, mostrar correcto
if (volumen_esfera<radio):
    print("incoherente")
if (volumen_esfera==radio):
    print("coincidencia")
if (volumen_esfera>radio):
    print("corrcecto")
