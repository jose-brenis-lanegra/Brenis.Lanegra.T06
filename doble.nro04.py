import os

precio,cantidad=0.0,0.0

#input
precio=float(os.sys.argv[1])
cantidad=float(os.sys.argv[2])

#processing
precio_total=precio*cantidad

#outpout
print("#####################################################")
print("#hallar el precio total de la cantidad de naranjas")
print("#####################################################")
print("#")
print("#####################################################")
print("#precio                               s/.:", precio)
print("#cantidad                                :", cantidad)
print("#precio total                         s/.:", precio_total)
print("#####################################################")

#condicional doble

#si la cantidad de naranjas es menor que 100 se aumentara un 7%
if (cantidad<100):
    aumento=(5*cantidad)/100
    print("el aumento es:", aumento)
else:
    print("no hay aumento")
