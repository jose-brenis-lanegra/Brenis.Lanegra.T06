import os

lado1,lado2,lado3,lado4=0,0,0,0

#input
lado1=float(os.sys.argv[1])
lado2=float(os.sys.argv[2])
lado3=float(os.sys.argv[3])
lado4=float(os.sys.argv[4])

#processing
perimetro_cuadrilatero=lado1+lado2+lado3+lado4

#outpout
print("###########################################")
print("#hallar el perimetro de un cuadrilatero")
print("###########################################")
print("#")
print("###########################################")
print("#primer lado                      :", lado1)
print("#segundo lado                     :", lado2)
print("#tercer lado                      :", lado3)
print("#cuarto lado                      :", lado4)
print("#perimetro                        :", perimetro_cuadrilatero)
print("###########################################")

#condicional multiple
#si los lados son diferentes , es un cuadrilatero normal
#si los lados paralelos son iguales, es un rectangulo
#si todos los lados son iguales , es un cuadrado
if (lado1!=lado2!=lado3!=lado4):
    print("es un cuadrilatero normal")
if (lado1==lado3 or lado2==lado4):
    print("es un rectangulo")
if (lado1==lado2==lado3==lado4):
    print("es un cuadrado")
