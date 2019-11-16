import os

arista=0.0

#input
arista=float(os.sys.argv[1])

#processing
area=5*(3**(1/2))*(arista**2)
volumen=(5*(3+(5**(1/2)))*(arista**3))/12

#outpout
print("#################################################")
print("#hallar el area y volumen de un icosaedro")
print("#################################################")
print("#")
print("#################################################")
print("#arista                         :", arista)
print("#area                           :", area)
print("#volumen                        :", volumen)
print("#################################################")

#condicional doble
#si la diferencia entre el area y volumen es positiva mostar mayor de lo contrario mostrar menor
if (volumen-area>0):
    print("mayor")
else:
    print("menor")
