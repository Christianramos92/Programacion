while True:
    edad = int(input("Ingrese una edad entre 1 y 100"))
    if edad>=1 and edad<=100:
        break
    print("Edad invalida, intente otra vez")
if edad>= 65:
    print("Tercera edad")
elif edad>=18:
    print("Mayor de edad")
else:
    print("Menor de edad")
 