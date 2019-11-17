import os

arista,altura=0,0

#input
arista=int(os.sys.argv[1])
altura=int(os.sys.argv[2])

#processing
volumen_piramide=((arista**2)*altura)/3

#outpout
print("#######################################")
print("#hallar el volumen de una piramide")
print("#######################################")
print("#")
print("#######################################")
print("#arista                       :", arista)
print("#altura                       :", altura)
print("#volumen                      :", volumen_piramide)
print("#######################################")

#condicion multiple
#si el volumen es menor que 500, entonces la piramide es de tipo 01
#si el volumen es desde 500 hasta 10000, entonces la piramide es de tipo 02
#si el volumen es mayor que 10000, entonces la piramide es de tipo 03
if (volumen_piramide<500):
    print("piramide tipo 01")
if (500<=volumen_piramide<=10000):
    print("piramide tipo 02")
if (volumen_piramide>10000):
    print("piramide tipo 03")
