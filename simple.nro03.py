import os

temperatura_fahrenheit=0.0

#input
temperatura_fahrenheit=float(os.sys.argv[1])

#processing
temperatura_celsius=((temperatura_fahrenheit-32)*5)/9

#outpout
print("################################################")
print("#calcular la temperatura de una persona joven   ")
print("################################################")
print("#")
print("################################################")
print("#temperatura en fahrenheit         :", temperatura_fahrenheit)
print("#temperatura en celsius            :", temperatura_celsius)
print("################################################")

#condicional simple

#si supera los 37.5 celsius , mostar "tiene fiebre"
if (temperatura_celsius>37.5):
    print("tiene fiebre")
