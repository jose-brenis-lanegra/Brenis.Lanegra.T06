import os

peso_boxeador01,peso_boxeador02=0.0,0.0

#input
peso_boxeador01=float(os.sys.argv[1])
peso_boxeador02=float(os.sys.argv[2])

#outpout
print("#######################################")
print("#peso de dos boxeadores en una lucha")
print("#######################################")
print("#")
print("#######################################")
print("#primer boxeador               :", peso_boxeador01)
print("#segundo boxeador              :", peso_boxeador02)
print("#######################################")

#condicional doble

#si tienen una diferencia menor o igual a 5kg la lucha es equitativ, de lo contrario es desigual
if (-5<=peso_boxeador01-peso_boxeador02<=5):
    print("combate pareja")
else:
    print("combate desigual")
