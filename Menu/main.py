# main.py


def mostrar_menu():
    print("\n===== MENÚ PRINCIPAL - ESCUELA =====")
    print("1. Registrar estudiante")
    print("2. Registrar notas")
    print("3. Calcular promedio de estudiante")
    print("4. Listar estudiantes")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            # Llamar a la función de registrar estudiante
            nombre = input("Nombre del estudiante: ")
            edad = int(input("Edad: "))
            
            # llamar funcion
            print(f"Estudiante {nombre} registrado correctamente.")

        elif opcion == "2":
            estudiante = input("Nombre del estudiante: ")
            materia = input("Materia: ")
            nota = float(input("Nota: "))
             # llamar funcion

        elif opcion == "3":
            estudiante = input("Nombre del estudiante: ")
              # llamar funcion

        elif opcion == "4":
              # llamar funcion
              print("listado de estudiantes")

        elif opcion == "5":
            print("Saliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("⚠️ \n Opción inválida, intenta nuevamente.")

if __name__ == "__main__":
    main()
