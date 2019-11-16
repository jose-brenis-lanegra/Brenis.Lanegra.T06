import os

arista=0.0

#input
arista=float(os.sys.argv[1])

#porcessing
area=3*((25+10*(5**(1/2)))**(1/2))*(arista**2)
volumen=((15+(7*(5**(1/2))))*(arista**3))/4

#outpout
print("#################################################")
print("#hallar el area y volumen de un dodecaedro")
print("#################################################")
print("#")
print("#################################################")
print("#arista                           :", arista)
print("#area                             :", area)
print("#volumen                          :", volumen)
print("#################################################")

#condicional doble
#si el volumen es diferente del area esta corecto, de lo contrario colocar coincidencia
if (volumen!=area):
    print("corecto")
else:
    print("coincidencia")
