import os 

pi,radio,altura=0.0,0,0

#input
pi=float(os.sys.argv[1])
radio=int(os.sys.argv[2])
altura=int(os.sys.argv[3])

#processing
generatriz=(radio*2+altura*2)**(1/2)
area_lateral_cono=pi*radio*generatriz

#outpout
print("#####################################")
print("#hallar el area lateral del cono")
print("#####################################")
print("#")
print("#####################################")
print("#radio                      :", radio)
print("#altura                     :", altura)
print("#generatriz                 :", generatriz)
print("#area lateral cono          :", area_lateral_cono)
print("#####################################")

#condicion multiple
#si la generatriz es igual a la altura, entonces el cono es inexistente
#si la generatriz es igual al radio, entonces el cono es incogruente
#si la altura es igual a la altura, entonces el cono es proporcional
if (generatriz==altura):
    print("inexistente")
if (generatriz==radio):
    print("incogruente")
if (altura==radio):
    print("proporcional")
