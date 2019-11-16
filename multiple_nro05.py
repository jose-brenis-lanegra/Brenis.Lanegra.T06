import os

largo,ancho,altura=0,0,0

#input
largo=int(os.sys.argv[1])
ancho=int(os.sys.argv[2])
altura=int(os.sys.argv[3])

#processing
volumen_prisma=largo*ancho*altura

#outpout
print("###############################")
print("#hallar el volumen del prisma")
print("###############################")
print("#")
print("###############################")
print("#largo                  :", largo)
print("#ancho                  :", ancho)
print("#altura                 :", altura)
print("#volumen                :", volumen_prisma)
print("###############################")

#condicional multiple
#si el volumen pasa de 1000 , es un primsa enorme
#si el volumen  pasa de 500 pero no de 100, es un prisma mediano
#si el volumen es menor o igual de 500, es un prisma pequeño
if (volumen_prisma>1000):
    print("prisma enorme")
if (1000>=volumen_prisma>500):
    print("prisma mediano")
if (volumen_prisma<=500):
    print("prisma pequeño")
