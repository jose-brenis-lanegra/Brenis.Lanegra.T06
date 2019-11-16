import os

arista=0.0

#input
arista=float(os.sys.argv[1])

#processing
area=2*(3**(1/2))*(arista**2)
volumen=((2**(1/2))*(arista**3))/3

#outpout
print("################################################")
print("#hallar el area y el volumen de un octaedro")
print("################################################")
print("#")
print("################################################")
print("#arista                              :", arista)
print("#area                                :", area)
print("#volumen                             :", volumen)
print("################################################")

#condicional doble
#si el area es menor que el volumen, esta corecto de lo contrario mostrar error
if (area<volumen):
    print("correcto")
else:
    print("error")
