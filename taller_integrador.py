#Sistema de Gestión Básica de Estudiantes
#funcion registrar estudiantes(nombre, edad, nota1, nota2, nota3)
def registrar_estudiantes(nombre, edad, nota1, nota2, nota3):
    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3
    }
    return estudiante
#funcion calcular promedio(nota1, nota2, nota3)
def calcular_promedio(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3) / 3
    return promedio
# funcion determinar estado >=4.0 aprobado, >=3.0 y < 4.0 En recuperación, <3.0 reprobado
def determinar_estado(promedio):
    if promedio >= 4.0:
        return "Aprobado"
    elif promedio >= 3.0:
        return "En recuperación"
    else:
        return "Reprobado"
# menu principal
def menu(): 
    estudiantes = []
    while True:
        print("1. Registrar estudiante")
        print("2. Calcular promedio y estado")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Ingrese el nombre del estudiante: ")
            edad = int(input("Ingrese la edad del estudiante: "))
            nota1 = float(input("Ingrese la nota 1: "))
            nota2 = float(input("Ingrese la nota 2: "))
            nota3 = float(input("Ingrese la nota 3: "))
            estudiante = registrar_estudiantes(nombre, edad, nota1, nota2, nota3)
            estudiantes.append(estudiante)
            print("Estudiante registrado exitosamente.")
        
        elif opcion == "2":
            for estudiante in estudiantes:
                promedio = calcular_promedio(estudiante["nota1"], estudiante["nota2"], estudiante["nota3"])
                estado = determinar_estado(promedio)
                print(f"Estudiante: {estudiante['nombre']}, Promedio: {promedio:.2f}, Estado: {estado}")
        
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Por favor, intente nuevamente.")
if __name__ == "__main__":
    menu()