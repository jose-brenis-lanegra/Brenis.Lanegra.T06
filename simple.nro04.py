import os

usuario,contrasena="",""

#input
usuario=(os.sys.argv[1])
contrasena=(os.sys.argv[2])

#outpout
print("##################################")
print("#ingresar a la cuenta del banco")
print("##################################")
print("#")
print("##################################")
print("#usuario             :", usuario)
print("#contraseña          :", contrasena)
print("##################################")

#condicional simple

#si el usuario es"pepe1306" y la contraseña "invasion2411", mostrar "acceso aceptado"
if (usuario=="pepe1306" and contrasena=="invasion2411"):
    print("acceso aceptado")
