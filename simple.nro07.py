import os

tipo_empleado,categoria="",""

#input
tipo_empleado=(os.sys.argv[1])
categoria=(os.sys.argv[2])

#outpout
print("################################################")
print("#descubrir el tipo y categoria de un empleado")
print("################################################")
print("#")
print("################################################")
print("#tipo de empleado               :", tipo_empleado)
print("#categoria                      :", categoria)
print("################################################")

#condicional simple

#si el tipo de empleado es "aux" y su categoria es "tc", mostrar "descente"
if (tipo_empleado=="aux" and categoria=="tc"):
    print("descente")
