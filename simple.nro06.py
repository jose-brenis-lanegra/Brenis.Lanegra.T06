import os

preguntas_propuestas,preguntas_marcadas=0.0,0.0

#input
preguntas_propuestas=float(os.sys.argv[1])
preguntas_marcadas=float(os.sys.argv[2])

#porcessing
nota_final=(preguntas_marcadas/preguntas_propuestas)*20

#outpout
print("############################################")
print("#calcular la nota del examen de un alumno")
print("############################################")
print("#")
print("############################################")
print("#preguntas propuestas             :", preguntas_propuestas)
print("#preguntas marcadas               :", preguntas_marcadas)
print("#nota final                       :", nota_final)
print("############################################")

#condicional simple

#si es menor o igual a 10.5 , mostrar "desaprobo el curso"
if (nota_final<=10.5):
    print("desaprobo el curso")
