import os

ratings01,ratings02=0.0,0.0

#input
ratings01=float(os.sys.argv[1])
ratings02=float(os.sys.argv[2])

#outpout
print("#############################")
print("#los ratings de fox y espn")
print("#############################")
print("#")
print("#############################")
print("#ratings de fox       :", ratings01)
print("#ratings de espn      :", ratings02)
print("#############################")

#condicional doble

#si los ratings de fox supera a las de espn mostrar victoria, en lo contrario mostrar derrota
if (ratings01>ratings02):
    print("victoria")
else:
    print("derrota")
