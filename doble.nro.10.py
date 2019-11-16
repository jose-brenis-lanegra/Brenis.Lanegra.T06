import os

a,b,c=0,0,0

#input
a=int(os.sys.argv[1])
b=int(os.sys.argv[2])
c=int(os.sys.argv[3])

#processing
discriminante=(b**2)-(4*a*c)

#outpout
print("###############################################")
print("#hallar la discriminante de una ecuacion")
print("###############################################")
print("#")
print("###############################################")
print("#a                                :", a)
print("#b                                :", b)
print("#c                                :", c)
print("#discriminante                    :", discriminante)
print("###############################################")

#condicional doble
#si la discrimante es menor que cero entonces sus raices son complejas de lo contrario son realea
if (discriminante<0):
    print("raices complejas")
else:
    print("raices reales")
