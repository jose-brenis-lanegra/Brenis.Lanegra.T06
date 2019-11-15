import os

paciente,mortalidad="",0

#input
paciente=(os.sys.argv[1])
mortalidad=int(os.sys.argv[2])

#outpout
print("##################################################")
print("#la mortalidad de una enfermedad de un paciente")
print("##################################################")
print("#")
print("##################################################")
print("#paciente                              :", paciente)
print("#porcentaje de mortalidad              :", mortalidad)
print("##################################################")

#condicional doble

#si es de 50% a mas el paciente tiene pocas la de vivir, de lo contrario puede vivir
if (mortalidad>=50):
    print("no hay posibilidades q viva")
else:
    print("tiene las de vivir")
