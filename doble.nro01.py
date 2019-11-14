import os

nota01,nota02,nota03,nota04,nota05,nota06,nota07=0.0,0.0,0.0,0.0,0.0,0.0,0.0

#input
nota01=float(os.sys.argv[1])
nota02=float(os.sys.argv[2])
nota03=float(os.sys.argv[3])
nota04=float(os.sys.argv[4])
nota05=float(os.sys.argv[5])
nota06=float(os.sys.argv[6])
nota07=float(os.sys.argv[7])

#processing
nota_final=nota01+nota02+nota03+nota04+nota05+nota06+nota07

#outpout
print("#################################################")
print("#calcular la nota final del examen de analisis")
print("#################################################")
print("#")
print("#################################################")
print("#primera nota                         :", nota01)
print("#segunda nota                         :", nota02)
print("#tercera nota                         :", nota03)
print("#cuarta nota                          :", nota04)
print("#quinta nota                          :", nota05)
print("#sexta nota                           :", nota06)
print("#setima nota                          :", nota07)
print("#nota definitiva                      :", nota_final)
print("#################################################")

#condicional doble

#si tiene de 91 a mas de nota esta aprobado, de lo contrario desaprobo
if (nota_final>=91):
    print("aprobado")
else:
    print("desaprobo")
