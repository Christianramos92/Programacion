# Tarea práctica:Verificar si una persona es mayor de edad
#Estudiante: Christian Paúl Ramos Rosario

def verificar_mayor_edad(anio_nacimiento, anio_actual):
    edad = anio_actual - anio_nacimiento

    if edad >= 18:
        resultado  = "La persona es MAYOR de edad."
    else:
        resultado = "La persona es menor de edad."
    return resultado

if __name__ == "__main__":
    anio_nacimiento = 2006
    anio_actual = 2026

    mensaje_final = verificar_mayor_edad(anio_nacimiento, anio_actual)
    print("--- VERIFICACIÓN DE EDAD---")
    print(f"Año de nacimiento:{anio_nacimiento}")
    print(f"Año atual:{anio_actual}")
    print(f"Resultado:{mensaje_final}")

    