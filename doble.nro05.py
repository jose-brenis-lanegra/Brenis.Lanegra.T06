import os

ciudad,clima="",""

#input
ciudad=(os.sys.argv[1])
clima=(os.sys.argv[2])

#outpout
print("##########################")
print("#el clima de una ciudad")
print("##########################")
print("#")
print("##########################")
print("#ciudad       :", ciudad)
print("#clima        :", clima)
print("##########################")

#condicional doble

#si la ciudad es ferreñafe su clima es caluroso, de lo contrario es falso
if (ciudad=="ferreñafe"):
    a=clima=="caluroso"
    print(a)
else:
    print("no es ferreñafe")
