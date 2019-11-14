import os

nro_tickets=0

#input
nro_tickets=int(os.sys.argv[1])

#outpout
print("##############################################")
print("#la cantidad de tickets ganados en la feria")
print("##############################################")
print("#")
print("##############################################")
print("#numero de tickets              :", nro_tickets)
print("##############################################")

#condicional simple

#si supera o iguala los 385 tickets, mostrar "te ganaste un pollo a la brasa"
if (nro_tickets>=385):
    print("te ganaste un pollo a la brasa")
