from services.gestion_notas import GestionNotas
from services.gestion_estudiantes import GestionEstudiantes
from services.validacion import Validacion

def menu():
    gestion_estudiantes = GestionEstudiantes()
    gestion_notas = GestionNotas()
    validacion = Validacion()

    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Registrar estudiante")
        print("2. Registrar nota")
        print("3. Calcular promedio de un estudiante")
        print("4. Listar estudiantes")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        # Validar opción del menú
        opciones_validas = ["1", "2", "3", "4", "5"]
        valido, mensaje_error = validacion.validar_opcion_menu(opcion, opciones_validas)
        if not valido:
            print(f"Error: {mensaje_error}")
            continue

        if opcion == "1":
            # Validar nombre
            while True:
                nombre = input("Nombre del estudiante: ")
                valido, mensaje_error = validacion.validar_nombre(nombre)
                if valido:
                    break
                print(f"Error: {mensaje_error}")

            # Validar edad
            while True:
                edad_input = input("Edad: ")
                valido, resultado = validacion.validar_edad(edad_input)
                if valido:
                    edad = resultado
                    break
                print(f"Error: {resultado}")

            # Validar matrícula
            while True:
                matricula = input("Matrícula: ")
                valido, mensaje_error = validacion.validar_matricula(matricula)
                if valido:
                    break
                print(f"Error: {mensaje_error}")

            gestion_estudiantes.registrar_estudiante(nombre, edad, matricula)
            print("✅ Estudiante registrado exitosamente")

        elif opcion == "2":
            matricula = input("Matrícula del estudiante: ")
            estudiante = gestion_estudiantes.obtener_estudiante(matricula)
            if estudiante:
                # Validar materia
                while True:
                    materia = input("Materia: ")
                    valido, mensaje_error = validacion.validar_materia(materia)
                    if valido:
                        break
                    print(f"Error: {mensaje_error}")

                # Validar nota
                while True:
                    nota_input = input("Nota: ")
                    valido, resultado = validacion.validar_nota(nota_input)
                    if valido:
                        nota = resultado
                        break
                    print(f"Error: {resultado}")

                gestion_notas.registrar_nota(estudiante, materia, nota)
                print(" Nota registrada exitosamente")
            else:
                print(" No se encontró el estudiante.")

        elif opcion == "3":
            matricula = input("Matrícula del estudiante: ")
            estudiante = gestion_estudiantes.obtener_estudiante(matricula)
            if estudiante:
                promedio = gestion_notas.calcular_promedio(estudiante)
                print(f" Promedio del estudiante: {promedio:.2f}")
            else:
                print(" No se encontró el estudiante.")

        elif opcion == "4":
            gestion_estudiantes.listar_estudiantes()

        elif opcion == "5":
            print(" Saliendo del sistema...")
            break

if __name__ == "__main__":
    menu()