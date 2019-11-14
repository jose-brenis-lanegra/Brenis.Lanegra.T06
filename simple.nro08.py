import os

correo=0

#input
correo=float(os.sys.argv[1])

#outpout
print("##############################################")
print("#calcular el numero de correos electronicos")
print("##############################################")
print("#")
print("##############################################")
print("#cantidad de correos electronicas:", correo)
print("##############################################")

#condicional simple

#si supera 1331 , cobrar 5 soles por el exceso de los correos
if (correo>1331):
    extra=2*(correo-1331)
    print("el cobro por los extras es:", extra)
