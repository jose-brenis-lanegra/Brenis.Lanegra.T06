import os

pi,radio=0.0,0.0

#input
pi=float(os.sys.argv[1])
radio=float(os.sys.argv[2])

#processing
area_circulo=pi*(radio**2)

#outpout
print("###############################")
print("#hallar el area del circulo")
print("###############################")
print("#")
print("###############################")
print("#valor de pi           :", pi)
print("#radio                 :", radio)
print("#area                  :", area_circulo)
print("###############################")

#condicional multiple
#si el area es mayor de 100, se considera un circulo grande
#si el area es mayor de 50 pero menor igual a 100, se considera un circulo mediano
#si el area no es mayor o igual que 50, se considera un circulo pequeño
if (area_circulo>100):
    print("circulo grande")
if (100>=area_circulo>50):
    print("circulo mediano")
if (area_circulo<=50):
    print("circulo pequeño")
