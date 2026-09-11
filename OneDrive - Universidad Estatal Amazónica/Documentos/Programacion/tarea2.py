contraseñacorrecta="12345cr"
intentos=0
acceso=False
 
while intentos < 3:
    contraseña=input("ingrese contraseña")
    intentos +=1
 
    if contraseña == contraseñacorrecta:
        acceso=True
        break
    else:
        print ("contraseña incorrecta")
        print ("intentos restantes",3-intentos)
 
if acceso:
    print ("acceso permitido")
else:
    print ("acceso bloqueado")
 