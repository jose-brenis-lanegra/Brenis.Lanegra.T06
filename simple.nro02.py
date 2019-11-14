import os

peso01,peso02=0.0,0.0

#imput
peso01=float(os.sys.argv[1])
peso02=float(os.sys.argv[2])

#processing
aumento=peso02-peso01

#outpout
print("########################################################")
print("#Descubrir el aumento de peso de una persona de 1.75m")
print("########################################################")
print("#")
print("########################################################")
print("#peso anterior                               :", peso01)
print("#peso actual                                 :", peso02)
print("#aumento                                     :", aumento)
print("########################################################")

#condicional simple

#si aumenta 19 kilos, mostrar que debe de hacer dieta urgente
if (aumento>19):
    print("porfavor hacer dieta urgente")
