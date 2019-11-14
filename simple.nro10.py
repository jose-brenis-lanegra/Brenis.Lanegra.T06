import os

monto,sector=0.0,""

#input
monto=float(os.sys.argv[1])
sector=(os.sys.argv[2])

#outpout
print("#################################")
print("#monto y sector de un empleado")
print("#################################")
print("#")
print("#################################")
print("#monto                :", monto)
print("#sector               :", sector)
print("#################################")

#condicional simple

#si el sector es privado , considere un aumento de 44% del monto
if (sector=="privado"):
    aumento=(44*monto)/100
    print("el aumento dado es:", aumento)
