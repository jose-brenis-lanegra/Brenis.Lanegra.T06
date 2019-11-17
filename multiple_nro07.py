import os

pi,altura,radio=0.0,0.0,0.0

#input
pi=float(os.sys.argv[1])
altura=float(os.sys.argv[2])
radio=float(os.sys.argv[3])

#processing
area_total_cilindro=2*pi*radio*(radio + altura)

#outpout
print("#####################################")
print("#hallar el area total del cilindro")
print("#####################################")
print("#")
print("#####################################")
print("#el valor de pi             :", pi)
print("#altura                     :", altura)
print("#radio                      :", radio)
print("#area total                 :", area_total_cilindro)
print("#####################################")

#condicional multiple
#si la altura es menor al radio, entonces su area es de pequeña proporcion
#si la altura es mayor al doble del radio, entonces su area es de gran proporcion
#si no es ninguna de las anteriores, entonces su area es de proporcion correcta
if (altura<radio):
    print("pequeña porprocion")
if (altura>2*radio):
    print("gran proporcion")
if (radio<=altura<=2*radio):
    print("proporcion correcta")
