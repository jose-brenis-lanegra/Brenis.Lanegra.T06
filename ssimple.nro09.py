import os

dias_libres,pago_diario=0.0,0.0
#input
dias_libres=float(os.sys.argv[1])
pago_diario=float(os.sys.argv[2])

#outpout
print("#####################################################")
print("#dias de vacaciones y pago diario de un trabajador")
print("#####################################################")
print("#")
print("#####################################################")
print("#dias de vacaciones                    :", dias_libres)
print("#pago diario                           :", pago_diario)
print("#####################################################")

#condicional simple

#si sus vacaiones son mas de 31 dias, descontar el 13% de su pago por sus extras
if (dias_libres>31):
    descuento=13*(dias_libres-31)/100
    print("la cantidad descontada es:", descuento)
